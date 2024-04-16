import speech_recognition as sr
import moviepy.editor
import subprocess
from googletrans import Translator


# video_path = r"demo/Tere Hawale 2nd Version (Without Music) _ Arijit Singh.mp4"
# video_clip = moviepy.editor.VideoFileClip(video_path)
# audio_clip = video_clip.audio
# audio_file_path = "outputs/output_audio.wav"
# audio_clip.write_audiofile(audio_file_path)


# command = f"whisper {audio_file_path} --model medium"

# process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

# # Get the output
# output = process.stdout

# print("Output:", output)


def mytext(vid_path):
    video_path = vid_path
    video_clip = moviepy.editor.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_file_path = "outputs/output_audio.wav"
    audio_clip.write_audiofile(audio_file_path)


    command = f"whisper {audio_file_path} --model medium"

    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

    # Get the output
    output = process.stdout
    # Initialize the translator
    translator = Translator()

    # Open the file and read its contents
    with open('/content/output_audio (1).txt', 'r') as tr:
        text = tr.read()

    translation = translator.translate(text, dest='en',src = 'ur')

    print("Translation:", translation.text)
    return translation.text
