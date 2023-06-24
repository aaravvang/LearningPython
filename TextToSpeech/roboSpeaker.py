from gtts import gTTS
message = input("Enter the message you want the robot to speak.")
speech = gTTS(message)
speech.save("Audio.mp3")
