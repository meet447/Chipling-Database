# Chipling-Database

This is the README for a Python database project that provides a web-based user interface for creating and managing projects and user accounts. The project is built using Flask, a Python web framework, and it allows users to register, log in, create projects, and store data associated with those projects. Below, you'll find detailed information on how to set up, use, and contribute to this project.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Register](#register)
  - [Log In](#log-in)
  - [Create Project](#create-project)
  - [View Projects](#view-projects)
  - [Store Data](#store-data)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Python Database Project is a web application built using Flask, a popular Python web framework. It provides users with the ability to register accounts, log in, create projects, and store data associated with those projects. The project is designed to be a simple and customizable database management system.

## Features

- **User Registration**: Users can create accounts by providing a unique username and a password.

- **User Authentication**: Users can log in securely using their registered credentials.

- **Project Creation**: Logged-in users can create projects by providing a project name and a project key.

- **Data Storage**: Users can store data associated with their projects. Data is stored in JSON format within project-specific files.

- **User Sessions**: User sessions are managed using Flask's built-in session management.

## Getting Started

### Prerequisites

Before you can run the project, you need to have the following prerequisites installed on your system:

- Python (3.10 recommended)
- Flask (Python web framework)

### Installation

Follow these steps to set up and run the project:

1. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/meet447/Chipling-Database.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Chipling-Database
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set the Flask secret key in the `app.py` file:

   ```python
   app.secret_key = "YourSecretKeyHere"
   ```

   Replace `"YourSecretKeyHere"` with a secure secret key of your choice.

7. Run the Flask application:

   ```bash
   python app.py
   ```

   The project should now be running locally at `http://localhost:5000`.

## Usage

### Register

To create a new user account:

1. Access the registration page by navigating to `http://localhost:5000/register` in your web browser.

2. Fill in the registration form with a unique username and a password.

3. Click the "Register" button.

   Note: You will receive a message if the chosen username is already in use.

### Log In

To log in to your account:

1. Access the login page by navigating to `http://localhost:5000/login` in your web browser.

2. Enter your username and password.

3. Click the "Log In" button.

   Note: You will receive an "Invalid login credentials" message if the provided credentials are incorrect.

### Create Project

Once logged in, you can create a new project:

1. Access the project creation page by navigating to `http://localhost:5000/create` in your web browser.

2. Enter a project key and a project name.

3. Click the "Create" button.

### View Projects

You can view your projects on the home page:

1. After logging in, you will be redirected to the home page at `http://localhost:5000/home`.

2. You will see a list of your created projects.

### Store Data

To store data within a project:

1. Click on the project name on the home page to access the project page at `http://localhost:5000/project/<project_id>`.

2. Provide the required data and click the "Save" button.

   Note: You may need to enter the project key to access the project page.

## Contributing

Contributions to this project are welcome. If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your changes:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Make your changes and commit them with clear and concise commit messages.

5. Push your changes to your forked repository on GitHub:

   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a pull request from your branch to the main project repository.

7. Your pull request will be reviewed, and if accepted, your changes will be merged.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
