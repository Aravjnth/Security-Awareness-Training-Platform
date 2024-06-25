import random
import json

class SecurityAwarenessTrainingPlatform:
    def __init__(self, training_data_file):
        self.training_data_file = training_data_file
        self.training_data = self.load_training_data()
        self.user_progress = {}

    def load_training_data(self):
        try:
            with open(self.training_data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File '{self.training_data_file}' not found")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in file '{self.training_data_file}' - {e}")
            return {}

    def get_random_question(self, category):
        if category in self.training_data:
            questions = self.training_data[category]
            return random.choice(questions)
        else:
            print(f"Error: Category '{category}' not found in training data")
            return None

    def ask_question(self, user, category):
        question = self.get_random_question(category)
        if question:
            print(f"Question: {question['question']}")
            answer = input("Enter your answer: ")
            if answer.lower() == question['answer'].lower():
                print("Correct!")
                self.update_progress(user, category, True)
            else:
                print(f"Incorrect. The correct answer is {question['answer']}.")
                self.update_progress(user, category, False)

    def update_progress(self, user, category, correct):
        if user not in self.user_progress:
            self.user_progress[user] = {}
        if category not in self.user_progress[user]:
            self.user_progress[user][category] = {'correct': 0, 'total': 0}
        self.user_progress[user][category]['total'] += 1
        if correct:
            self.user_progress[user][category]['correct'] += 1

    def display_progress(self, user):
        if user in self.user_progress:
            print(f"Progress for {user}:")
            for category, stats in self.user_progress[user].items():
                print(f"  {category}: {stats['correct']} / {stats['total']}")
        else:
            print(f"Error: User '{user}' not found in progress data")

    def train_user(self, user, categories):
        for category in categories:
            self.ask_question(user, category)

# Example usage
training_data_file = 'training_data.json'
platform = SecurityAwarenessTrainingPlatform(training_data_file)

user = 'john'
categories = ['phishing', 'password_security', 'data_protection']

platform.train_user(user, categories)
platform.display_progress(user)