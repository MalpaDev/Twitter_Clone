# Twitter_Clone
A distributed Publish–Subscribe application built using the MQTT protocol, 
simulating a Twitter-like platform where users can post tweets and subscribe 
to hashtags for real-time updates.

## Objectives
- This project demonstrates the Pub/Sub communication model through MQTT, enabling:
- Real-time tweet publishing and delivery
- Topic-based subscription using hashtags
- GUI interfaces for both publishers and subscribers

## Features
#### Publisher
- GUI built with Tkinter
- Input fields for:
    - Username
    - Tweet Message
    - Hashtag
- Publish button
- Publishes to an MQTT Broker (using Mosquitto on localhost)
#### Subscriber
- GUI for following hashtags/topics
- Input fields for Hashtag topics
- Buttons to:
    - Subscribe
    - Unsubscribe
- Real-time tweet feed area displaying all recieved messages