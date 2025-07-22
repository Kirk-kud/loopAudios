# **Loop Audio Project**

This project is to scratch a very particular itch I have had for a while. I usually want to create hour long loops of a particular song or recording 
but face website riddled with adds and long waiting times before I could achieve. I decided to build a simple Python script to achieve this much quicker.

### **Version 1: **
Using Pydub, which was not available in Python version 3.13.3, I had to downgrade to version 3.12.3 to complete this project.
The project employs a simple command line interface which allows the user to pick a file from their local directories and
then allows them to create a loop that spans between **1 to 5 hours**. When the looping is done, the audio is exported into the project folder.
The script currently allows three audio types: 
- .mp3
- .m4a
- .wav
