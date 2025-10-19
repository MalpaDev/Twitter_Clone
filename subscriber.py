"""
subscriber.py
notes go hear
"""
import tkinter as tk
from tkinter import messagebox

class Subscriber:
    def __init__(self, root):
        self.root = root
        root.title("MQTT Twitter - Subscriber")

        tk.Label(root, text = "Hashtag:").grid(row = 0, column = 0, sticky = "e", padx = 5, pady = 5)
        self.hashtag_entry = tk.Entry(root, width = 30)
        self.hashtag_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        button_frame = tk.Frame(root)
        button_frame.grid(row = 1, column = 1, pady = 5)
        tk.Button(button_frame, text = "Subscribe", command = self.subscribe).pack(side = "left", padx = 5)
        tk.Button(button_frame, text = "Unsubscribe", command = self.unsubscribe).pack(side = "left", padx = 5)

        tk.Label(root, text = "Tweet Feed: ").grid(row = 2, column = 0, sticky = "ne", padx = 5, pady = 5)
        self.feed_box = tk.Text(root, width = 50, height = 10, state = "disabled")
        self.feed_box.grid(row = 2, column = 1, padx = 5, pady = 5)

    def subscribe(self):
        hashtag = self.hashtag_entry.get().strip()
        if not hashtag:
            messagebox.showwarning("Missing Info", "Please enter a hashtag to subscribe to.")
            return
        print(f"Subscribed to #{hashtag}")
        self.display_message(f"Subscribed to #{hashtag}\n")

    def unsubscribe(self):
        hashtag = self.hashtag_entry.get().strip()
        if not hashtag:
            messagebox.showwarning("Missing Info", "Please enter a hashtag to subscribe to.")
            return
        print(f"Unsubscribed to #{hashtag}")
        self.display_message(f"Unsubscribed to #{hashtag}\n")

    def display_message(self, msg):
        self.feed_box.config(state = "normal")
        self.feed_box.insert(tk.END, msg)
        self.feed_box.config(state = "disabled")
        self.feed_box.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Subscriber(root)
    root.mainloop()