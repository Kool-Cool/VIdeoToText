import speech_recognition as sr
import moviepy.editor
from openai import OpenAI
import subprocess

video_path = r"demo\Tere Hawale 2nd Version (Without Music) _ Arijit Singh.mp4"
video_clip = moviepy.editor.VideoFileClip(video_path)
audio_clip = video_clip.audio
audio_file_path = "outputs/output_audio.wav"
audio_clip.write_audiofile(audio_file_path)


command = f"whisper {audio_file_path} --model medium"

process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

# Get the output
output = process.stdout

print("Output:", output)


def mytext(vid_path):
    video_path = r"vid_path"
    video_clip = moviepy.editor.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_file_path = "outputs/output_audio.wav"
    audio_clip.write_audiofile(audio_file_path)


    command = f"whisper {audio_file_path} --model medium"

    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

    # Get the output
    output = process.stdout
    return output













# # Initialize the recognizer
# r = sr.Recognizer()

# # Open the audio file
# with sr.AudioFile(audio_file_path) as source:
#     # Read the audio file
#     audio_data = r.record(source)
#     # Convert speech to text
#     try:
#         text = r.rec(audio_data, language='hi-IN')
#         print("Transcription:", text)
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand the audio.")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


""" 
# model = whisper.load_model("base")
# # print(model)
# tran = model.transcribe(r"output_audio.wav")

# print(tran['text']) """


