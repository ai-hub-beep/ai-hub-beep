import os
import subprocess
import sys

# List of required packages
required_packages = [
    'psutil',  # For system and resource monitoring
]

# Directory structure to create
directories = [
    'logs',  # Directory for log files
    'data',  # Directory for data files
    'configs',  # Directory for configuration files
]

# Basic configuration file content
basic_config_content = """# Configuration for the Autonomous AI
# Change these values based on your environment
restricted_paths = ['/path/to/restricted_directory', '/another/restricted/path']
data_directory = '/path/to/data_directory'
"""

def install_packages():
    """Install required Python packages."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *required_packages])
        print("All required packages installed successfully.")
    except Exception as e:
        print(f"Error installing packages: {e}")
        sys.exit(1)

def create_directories():
    """Create necessary directories for the project."""
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")

def create_config_file():
    """Create a basic configuration file."""
    config_file_path = 'configs/config.py'
    if not os.path.exists(config_file_path):
        with open(config_file_path, 'w') as config_file:
            config_file.write(basic_config_content)
        print(f"Created configuration file: {config_file_path}")
    else:
        print(f"Configuration file already exists: {config_file_path}")

def main():
    print("Starting installation of essential packages and directory setup...")
    install_packages()
    create_directories()
    create_config_file()
    print("Installation completed successfully.")

if __name__ == "__main__":
    main()
