This folder contains Python scripts for managing user data, user accounts, and user projects within the Chipling database system. Below is a brief overview of each script:

## data.py

`data.py` handles the creation and retrieval of user data. It includes functions for:

- `create_user(username, uid, key, id)`: Create a new user and store their information in a JSON file.
- `retrieve_users()`: Retrieve a list of all users from the JSON file.
- `search_users(id)`: Search for a user by their ID and return their information.

## login.py

`login.py` manages user accounts, including functions for:

- `create_useracc(name, id, uid)`: Create a new user account and store it in a JSON file.
- `retrieve_useracc()`: Retrieve a list of all user accounts from the JSON file.
- `search_login(uid)`: Search for a user account by their UID and return account details.
- `get_uid(username)`: Get the UID associated with a username.

## project.py

`project.py` is responsible for creating and managing user projects. It includes functions for:

- `create_project(id, key, name, uid)`: Create a new project folder and JSON file, storing project information.
- `retrieve_project(id, name, key)`: Retrieve project data from a JSON file within a specific project folder.
- `get_user_projects()`: Get a list of all user projects from a JSON file.
- `search_projects(uid)`: Search for projects associated with a specific user by UID.
- `get_project(id)`: Retrieve a specific project by its ID.

The scripts use JSON files to store and retrieve data related to users and projects. The folder structure is organized to facilitate data management.

Please make sure to refer to the script descriptions and function documentation for more details on their usage.

Note: Ensure that the `json_files` directory and `projects` directory exist in the same location as these scripts for proper file operations.

Feel free to update this readme as needed to include any additional information or usage instructions for these scripts.
