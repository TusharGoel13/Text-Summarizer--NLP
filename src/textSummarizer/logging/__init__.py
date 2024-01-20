import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Specify the directory for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the specified logging format

    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file (running_logs.log)
        logging.StreamHandler(sys.stdout)   # Log to the console (stdout)
    ]
)

# Create a logger instance with the name "textSummarizerLogger"
logger = logging.getLogger("textSummarizerLogger")
