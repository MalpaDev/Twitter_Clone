"""
main.py
notes go hear
"""

import tkinter as tk
import threading
from publisher import Publisher
from subscriber import Subscriber

class Launcher:
    def __init__(self, root):
        self.root = root
        root.title("MQTT Twitter Clone Launcher")
        root.geometry("300x180")

        tk.Label(root, text = "MQTT Twitter Clone", font = ("Segoe UI", 14, "bold")).pack(pady = 15)
        tk.Label(root, text = "Choose an option to open:").pack(pady = 5)

        tk.Button(root, text = "Open Publisher", width = 20, command = self.run_publisher).pack(pady = 5)
        tk.Button(root, text = "Open Subscriber", width = 20, command = self.run_subscriber).pack(pady = 5)
        tk.Button(root, text = "Exit", width = 20, command = root.destroy).pack(pady = 10)

    def run_publisher(self):
        threading.Thread(target = self.launch_publisher, daemon = True).start()

    def run_subscriber(self):
        threading.Thread(target = self.launch_subscriber, daemon = True).start()

    def launch_publisher(self):
        pub_root = tk.Tk()
        Publisher(pub_root)
        pub_root.mainloop()

    def launch_subscriber(self):
        sub_root = tk.Tk()
        Subscriber(sub_root)
        sub_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Launcher(root)
    root.mainloop()