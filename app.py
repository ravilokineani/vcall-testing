from streamlit_webrtc import webrtc_streamer
import av
import cv2

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        img = cv2.blur(img, (8,8))

        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="sample", video_processor_factory=VideoProcessor)