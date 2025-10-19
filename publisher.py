"""
publisher.py
notes go hear
"""
import tkinter as tk
from tkinter import messagebox

class Publisher:
    def __init__(self, root):
        self.root = root
        root.title("MQTT Twitter - Publisher")

        tk.Label(root, text = "Username:").grid(row = 0, column = 0, sticky = "e", padx = 5, pady = 5)
        self.username_entry = tk.Entry(root, width = 30)
        self.username_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        tk.Label(root, text = "Tweet:").grid(row = 1, column = 0, sticky = "ne", padx = 5, pady = 5)
        self.tweet_entry = tk.Text(root, width = 40, height = 5)
        self.tweet_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

        tk.Label(root, text = "Hashtag:").grid(row = 2, column = 0, sticky = "e", padx = 5, pady = 5)
        self.hashtag_entry = tk.Entry(root, width = 30)
        self.hashtag_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

        publish_button = tk.Button(root, text = "Publish Tweet", command = self.publish_tweet)
        publish_button.grid(row = 3, column = 1, pady = 10)

    def publish_tweet(self):
        username = self.username_entry.get().strip()
        tweet = self.tweet_entry.get("1.0", tk.END).strip()
        hashtag = self.hashtag_entry.get().strip()

        if not username or not tweet or not hashtag:
            messagebox.showwarning("Missing Info", "Please fill out all fields.")
            return
        
        # print to console
        print(f"Published: @{username} - \"{tweet}\" to topic #{hashtag}")
        messagebox.showinfo("Tweet Published", f"Tweet sent to #{hashtag}")
        self.tweet_entry.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Publisher(root)
    root.mainloop()