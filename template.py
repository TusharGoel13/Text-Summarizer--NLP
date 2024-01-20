import os
from pathlib import Path # Abstracts away the differences in path syntax between different operating systems.
import logging

# Configure logging to display INFO level messages with a specific format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name and a list of files to be created
project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",  # GitHub Actions workflow file to keep the directory structure
    f"src/{project_name}/__init__.py",  # Python package initialization file
    f"src/{project_name}/components/__init__.py",  # Components package initialization file
    f"src/{project_name}/utils/__init__.py",  # Utils package initialization file
    f"src/{project_name}/utils/common.py",  # Common utility file within the Utils package
    f"src/{project_name}/logging/__init__.py",  # Logging package initialization file
    f"src/{project_name}/config/__init__.py",  # Config package initialization file
    f"src/{project_name}/config/configuration.py",  # Configuration file within the Config package
    f"src/{project_name}/pipeline/__init__.py",  # Pipeline package initialization file
    f"src/{project_name}/entity/__init__.py",  # Entity package initialization file
    f"src/{project_name}/constants/__init__.py",  # Constants package initialization file
    "config/config.yaml",  # Configuration file for the project
    "params.yaml",  # Parameters file for the project
    "app.py",  # Main application file
    "main.py",  # Main script file
    "Dockerfile",  # Dockerfile for containerization
    "requirements.txt",  # File specifying project dependencies
    "setup.py",  # File for project setup and installation
    "research/trials.ipynb",  # Jupyter notebook for research trials
]

'''  Structure of above folders and files
__init__.py is a constructor file considered as local package

- .github/
  -> workflows/
    -> .gitkeep

- src/
  -> textSummarizer/
    -> __init__.py
    -> conponents/
      -> __init__.py
    -> utils/
      -> __init__.py
      -> common.py
    -> logging/
      -> __init__.py
    -> config/
      -> __init__.py
      -> configuration.py
    -> pipeline/
      -> __init__.py
    -> entity/
      -> __init__.py
    -> constants/
      -> __init__.py

- config/
  -> config.yaml

- params.yaml
- app.py
- main.py
- Dockerfile
- requirements.txt
- setup.py

- research/
  -> trials.ipynb

'''

# Iterate through the list of files and create directories and empty files if needed
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if the file doesn't exist or is empty, then create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    # If the file already exists, log a message
    else:
        logging.info(f"{filename} already exists")
