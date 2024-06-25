# Security Awareness Training Platform

## Overview

The Security Awareness Training Platform is a Python-based web application designed to educate users on cybersecurity best practices and awareness. This platform provides interactive modules, quizzes, and resources to help organizations and individuals improve their understanding of security threats, policies, and procedures.

## Features

- Interactive training modules on various cybersecurity topics.
- Quizzes and assessments to test knowledge retention.
- Dashboard for tracking progress and completion rates.
- Admin panel for managing users, courses, and content.
- Integration with learning management systems (LMS).
- Responsive web interface for accessibility across devices.

## Requirements

- Python 3.x
- Flask framework
- SQLAlchemy for database management
- Bootstrap or another frontend framework for UI design

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Security-Awareness-Training-Platform.git
    cd security-awareness-training
    ```

2. Set up the Python environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Initialize the database (SQLite example):
    ```bash
    python manage.py create_db
    ```

## Usage

1. Start the Flask development server:
    ```bash
    python manage.py runserver
    ```

2. Access the training platform in a web browser at `http://localhost:5000`.

3. Customize the platform by adding new modules, quizzes, and user accounts through the admin panel.

## Admin Panel

- Access the admin panel at `http://localhost:5000/admin` (default credentials may apply).

## Legal Disclaimer

This Security Awareness Training Platform is intended for educational purposes and training within authorized environments. It should not be used for malicious or unethical purposes. The developers assume no liability for any misuse or damage caused by this application.

## Contributing

Contributions to this project are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact me at www.linkedin.com/in/aravinth-aj
