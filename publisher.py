"""
publisher.py
Provides a Tkinter GUI that allows users to post "tweets"
to specific MQTT topics(hashtags). Each tweet is published
to a MQTT broker running on localhost. 
"""
import tkinter as tk
from tkinter import messagebox
from mqtt_handler import MQTTHandler

class Publisher:
    # Initializes the publisher GUI and connects to the MQTT broker
    def __init__(self, root):
        self.root = root
        root.title("MQTT Twitter - Publisher")
        # connection to MQTT
        self.mqtt = MQTTHandler()
        self.mqtt.connect()

        # Tkinter GUI
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

        # ensures clean disconnect
        root.protocol("WM_DELETE_WINDOW", self.on_close)

    # gets input fields and publishes to MQTT broker
    def publish_tweet(self):
        username = self.username_entry.get().strip()
        tweet = self.tweet_entry.get("1.0", tk.END).strip()
        topic = self.hashtag_entry.get().strip()

        if not username or not tweet or not topic:
            messagebox.showwarning("Missing Info", "Please fill out all fields.")
            return
        
        message = f"{username}: {tweet}"

        try:
            self.mqtt.publish(topic, message)
            print(f"Published: @{username} -> topic: {topic}")
            messagebox.showinfo("Tweet published", f"Tweet sent to {topic}")
            # clear tweet entry box
            self.tweet_entry.delete("1.0", tk.END)
        except Exception as e:
            print(f"Error publishing: {e}")
            messagebox.showerror("Error", f"Failed to publish tweet.\n{e}")

    def on_close(self):
        self.mqtt.disconnect()
        self.root.destroy()