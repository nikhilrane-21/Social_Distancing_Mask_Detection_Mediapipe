import cv2
from math import pow, sqrt


def distancing(faces, frame):
	highRisk = set()
	mediumRisk = set()

	if faces==None:
		return

	for face in faces:
		face.x, face.y, face.w, face.h = face.bbox[0], face.bbox[1], face.bbox[2], face.bbox[3]

	if len(faces)>=2:
		f1_x = faces[0].x
		f1_y = faces[0].y
		f2_x = faces[1].x
		f2_y = faces[1].y
		distanceOfBboxes = sqrt(pow(f2_x - f1_x, 2)+ pow(f2_y - f1_y, 2))

		if distanceOfBboxes < 300:
			highRisk.add(face.i), highRisk.add(face.j)
		if len(highRisk)!=0:
			cv2.putText(frame, "Maintain social Distancing", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
						(0, 0, 255), 2)

