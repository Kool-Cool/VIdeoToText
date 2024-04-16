"""  -------  SPEECH TO TEXT -------
"""
import speech_recognition as sr
# from googletrans import Translator
import moviepy.editor





# Convert video to audio

vid = r"demo\Tere Hawale 2nd Version (Without Music) _ Arijit Singh.mp4"
vid = moviepy.editor.VideoFileClip(vid)
aud = vid.audio
aud.write_audiofile("output_audio.wav")
# aud.write_audiofile("outputs/output_audio.wav")





import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# open the file
with sr.AudioFile(r'output_audio.wav') as source:
    # read the audio file
    audio_data = r.record(source)
    # convert speech to text
    text = r.recognize_google(audio_data, language='hi-IN')
    print(text)

print(" If there’s a long pause in the audio, it might stop transcribing at that point.")

