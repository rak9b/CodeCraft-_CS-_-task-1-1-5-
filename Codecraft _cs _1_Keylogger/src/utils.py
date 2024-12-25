import os
from datetime import datetime

def setup_logging(log_dir):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

def create_log_file(log_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(log_dir, f"keylog_{timestamp}.txt")
