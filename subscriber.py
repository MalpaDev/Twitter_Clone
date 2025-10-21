"""
subscriber.py
Connects to MQTT broker running on localhost and listens
for messages published to specific topics. Incoming tweets
are displayed in real time on a tkinter GUI.
"""
import tkinter as tk
from tkinter import messagebox
from mqtt_handler import MQTTHandler

class Subscriber:
    # Initalizes the GUI and connects to MQTT broker
    def __init__(self, root):
        self.root = root
        root.title("MQTT Twitter - Subscriber")

        # MQTT connection and registers on_message callback
        self.mqtt = MQTTHandler()
        self.mqtt.connect(on_message = self.on_message)

        # GUI
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

        # tracks active subscriptions
        self.subscribed_topics = set()

        # ensures clean disconnect
        root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    # Called when a new message arrives
    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        topic = msg.topic
        display_text = f"{topic}: {message}\n"
        print(f"Recieved -> {display_text.strip()}")
        self.display_message(display_text)

    def subscribe(self):
        topic = self.hashtag_entry.get().strip()
        if not topic:
            messagebox.showwarning("Missing Info", "Please enter a hashtag to subscribe to.")
            return
        if topic in self.subscribed_topics:
            messagebox.showinfo("Already Subscribed", f"You are already subscribed to {topic}")
            return
        
        self.mqtt.subscribe(topic)
        self.subscribed_topics.add(topic)
        self.display_message(f"Subscribed to {topic}\n")

    def unsubscribe(self):
        topic = self.hashtag_entry.get().strip()
        if not topic:
            messagebox.showwarning("Missing Info", "Please enter a hashtag to subscribe to.")
            return
        if topic not in self.subscribed_topics:
            messagebox.showinfo("Not Subscribed", f"You are not subscribed to {topic}")
            return
        
        self.mqtt.unsubscribe(topic)
        self.subscribed_topics.remove(topic)
        self.display_message(f"Unsubscribed from {topic}\n")

    # Adds new messages to the text field
    def display_message(self, msg):
        self.feed_box.config(state = "normal")
        self.feed_box.insert(tk.END, msg)
        self.feed_box.config(state = "disabled")
        self.feed_box.see(tk.END)

    def on_close(self):
        self.mqtt.disconnect()
        self.root.destroy()