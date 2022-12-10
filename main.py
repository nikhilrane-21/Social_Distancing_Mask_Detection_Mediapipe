import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Face detection
from detect_on_video import detect_mask
from face_detector import detect_faces
from social_distancing import distancing
# Utils
import cv2
from utils import print_fps, print_faces

pTime = [0]
input_dir = 0


if __name__ == "__main__":
    cap = cv2.VideoCapture(input_dir)
    cv2.namedWindow('PROCTORING ON')
    frames=[]
    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret :
            break

        print_fps(frame, pTime)
        faces = detect_faces(frame, confidence = 0.7)
        distancing(faces, frame)
        detect_mask(frame, faces)
        print_faces(frame, faces)

        cv2.imshow('Frame live',  frame)
        if cv2.waitKey(1) & 0xFF == 27: 
            break

    cap.release()
    cv2.destroyAllWindows()
