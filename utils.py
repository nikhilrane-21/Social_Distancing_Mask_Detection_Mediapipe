import cv2
import time
from face_detector import detect_faces

font = cv2.FONT_HERSHEY_SIMPLEX

def print_fps(frame, pTime):
    cTime = time.time()
    fps = 1/(cTime - pTime[0])
    pTime[0] = cTime
    cv2.putText(frame, f"FPS : {int(fps)}", (15,30),font, 0.5, (255,0,0),2)

def print_faces(frame, faces):
    if not faces:
        cv2.putText(frame, "No person Detected", (15, 130), font, 0.5, (0, 0, 255), 2)
        return

    for face in faces:
        x,y,w,h = face.origbbox
    
        #Face detection
        cv2.rectangle(frame, face.origbbox, (0, 0, 153), 2)
        # cv2.putText(frame, "c:"+str(round(face.confidence[0],4)),(x+w+5, y+28), cv2.FONT_HERSHEY_PLAIN, 1, (153,0,0), 1)
        cv2.putText(frame, "Face ID: "+str(face.id + 1), (x+w+5, y+h), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)

        if len(faces) != 1:
            cv2.putText(frame, "More than One Person Detected", (15, 130), font, 0.5, (0, 0, 255), 2)
