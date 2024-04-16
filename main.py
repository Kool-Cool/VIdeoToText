import streamlit as st
import cv2
from PIL import Image
import os
import speech_recognition as sr
from googletrans import Translator
from pydub import AudioSegment




""" -----  STRAMLIT SETUP ----- """
st.write('''
THIS IS IT !!

Get English Captions for any hindi Video 
''')


st.title('''
Upload the video !
''')
uploaded_video = st.file_uploader("Choose video", type=["mp4", "mov" ,"avi"])

if uploaded_video is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_video.read())
    
    vf = cv.VideoCapture(tfile.name)



st.title('''
Record Live ?
''')

if 'recording' not in st.session_state:
    st.session_state.recording = False

run = st.button('Start Recording')
if run:
    st.session_state.recording = True

close = st.button('Stop Recording')
if close:
    st.session_state.recording = False

if st.session_state.recording:
    cap = cv2.VideoCapture(0)  # 0 for the default camera 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
    out = cv2.VideoWriter('outputs/output.mp4', fourcc, 20.0, (640, 480))  # output file, fps, resolution
    # print(cap.isOpened())

    file_size_placeholder = st.empty()
    file_size_MB = None
    while(cap.isOpened() and st.session_state.recording):
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to stop recording
                    break
                # Check the size of the file
                file_size_MB = os.path.getsize('outputs/output.mp4') / (1024 * 1024)  # Convert bytes to MB
                # st.write(f"Current file size: {file_size_MB:.2f} MB")  # Display the file size
                file_size_placeholder.text(f"Current file size: {file_size_MB:.2f} MB")
                if file_size_MB > 100:  # Stop recording if size > 100 MB
                    st.write("File limit Exceeded (100 MB is the limit)")
                    break
            else:
                break
    file_size_MB = os.path.getsize('outputs/output.mp4') / (1024 * 1024)  # Convert bytes to MB
    st.write(f"Current file size: {file_size_MB:.2f} MB")  # Display the file size
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if os.path.exists('outputs/output.mp4'):
    file_size_MB = os.path.getsize('outputs/output.mp4') / (1024 * 1024)  # Convert bytes to MB
    st.write(f"Current file size: {file_size_MB:.2f} MB")  # Display the file size

st.title('''
Watch Demo !?
''')

