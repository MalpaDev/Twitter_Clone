"""
main.py
Launchs MQTT Twitter Clone Project
Creates a simple GUI where you can open multiple publisher and subscriber
instances. All instances are ran in seperate threads so they can operate
simultaneously and communicate through the local MQTT broker.
"""

import tkinter as tk
import threading
from publisher import Publisher
from subscriber import Subscriber

class Launcher:
    # Creates application window and the ability to create publisher and subscriber instances
    def __init__(self, root):
        self.root = root
        root.title("MQTT Twitter Clone Launcher")
        root.geometry("300x180")

        tk.Label(root, text = "MQTT Twitter Clone", font = ("Segoe UI", 14, "bold")).pack(pady = 15)
        tk.Label(root, text = "Choose an option to open:").pack(pady = 5)

        tk.Button(root, text = "Open Publisher", width = 20, command = self.run_publisher).pack(pady = 5)
        tk.Button(root, text = "Open Subscriber", width = 20, command = self.run_subscriber).pack(pady = 5)
        tk.Button(root, text = "Exit", width = 20, command = root.destroy).pack(pady = 10)

    # launchs publisher GUI in new thread
    def run_publisher(self):
        threading.Thread(target = self.launch_publisher, daemon = True).start()
    # launchs subscriber GUI in new thread
    def run_subscriber(self):
        threading.Thread(target = self.launch_subscriber, daemon = True).start()

    # creates new tkinter instance and runs the publisher GUI
    def launch_publisher(self):
        pub_root = tk.Tk()
        Publisher(pub_root)
        pub_root.mainloop()
    # creates new tkinter instance and runs the subscriber GUI
    def launch_subscriber(self):
        sub_root = tk.Tk()
        Subscriber(sub_root)
        sub_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Launcher(root)
    root.mainloop()