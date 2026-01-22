import speech_recognition as sr

recognizer = sr.Recognizer()

# Use an audio file instead of microphone (easy & safe)
audio_file = "audio.wav"

with sr.AudioFile(audio_file) as source:
    print("Processing audio file...")
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("\nTranscribed Text:")
    print(text)

except sr.UnknownValueError:
    print("Sorry, could not understand the audio")

except sr.RequestError as e:
    print("API error:", e)
