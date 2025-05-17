import os
import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.restart_app()
    
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"\n🔄 Обнаружено изменение в {os.path.basename(event.src_path)}, перезапуск...")
            self.restart_app()
    
    def restart_app(self):
        if self.process:
            self.process.terminate()
        os.system('cls')
        self.process = subprocess.Popen(
            [sys.executable, "-m", "app.client.main"],
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )

if __name__ == "__main__":
    print("🚀 hot-reload...")
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path="./app", recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        event_handler.process.terminate()
    observer.join()