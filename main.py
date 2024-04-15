import streamlit as st
import cv2
from PIL import Image

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

run = st.checkbox('Run')
st.write(" press q to stop recording")
if run:
    cap = cv2.VideoCapture(0)  # 0 for the default camera
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # codec
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # output file, fps, resolution

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to stop recording
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


st.title('''
Watch Demo !?
''')

