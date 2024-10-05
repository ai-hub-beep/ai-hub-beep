import os
import time
import psutil
import threading
import logging
import gzip
import shutil
from configs.config import restricted_paths, data_directory

# Set up logging
logging.basicConfig(
    filename='logs/ai_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class HealthMonitor:
    """Class to monitor the health of the system."""
    
    def check_health(self):
        """Check and return health metrics."""
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        return {
            'CPU Usage': cpu_usage,
            'Memory Usage': memory_usage,
            'Disk Usage': disk_usage
        }

class DataManager:
    """Class to manage data extraction and compression."""
    
    def register_data(self, data_name, file_name):
        """Register a data entry."""
        logging.info(f"Registered data: {data_name} in file: {file_name}")

    def log_data(self, data_name, content):
        """Log content to the specified data entry."""
        with open(os.path.join(data_directory, f"{data_name}.txt"), 'a') as file:
            file.write(content + '\n')
        logging.info(f"Logged data for {data_name}: {content}")

    def compress_data(self, file_name):
        """Compress the specified file using gzip."""
        with open(file_name, 'rb') as f_in:
            with gzip.open(f"{file_name}.gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        logging.info(f"Compressed {file_name} to {file_name}.gz")

class AutonomousAI:
    """Class to represent the autonomous AI system."""
    
    def __init__(self):
        self.health_monitor = HealthMonitor()
        self.data_manager = DataManager()
        self.control_thread = threading.Thread(target=self.control_loop)
        self.optimization_thread = threading.Thread(target=self.optimization_loop)
        self.running = True

    def control_loop(self):
        """Control loop for managing AI operations."""
        while self.running:
            health_metrics = self.health_monitor.check_health()
            logging.info(f"Health Metrics: {health_metrics}")
            time.sleep(5)  # Check health every 5 seconds

    def optimization_loop(self):
        """Optimization loop for the AI."""
        while self.running:
            logging.info("Optimizing system...")
            # Perform optimization tasks here
            time.sleep(10)  # Optimize every 10 seconds

    def start(self):
        """Start the AI system."""
        logging.info("Starting the Autonomous AI...")
        self.control_thread.start()
        self.optimization_thread.start()

    def stop(self):
        """Stop the AI system."""
        logging.info("Stopping the Autonomous AI...")
        self.running = False
        self.control_thread.join()
        self.optimization_thread.join()
        logging.info("Autonomous AI stopped.")

if __name__ == "__main__":
    autonomous_ai = AutonomousAI()
    try:
        autonomous_ai.start()
        while True:
            command = input("Type 'exit' to stop the AI: ")
            if command.lower() == 'exit':
                autonomous_ai.stop()
                break
    except KeyboardInterrupt:
        autonomous_ai.stop()
