import pyautogui
import cv2
import numpy as np
resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XivD")

filename = "Recording.mp4"

fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Screen Recorder", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Screen Recorder", 480, 270)

while True:
	img = pyautogui.screenshot()

	frame = np.array(img)

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	out.write(frame)
	
	cv2.imshow('Screen Recorder', frame)
	
	if cv2.waitKey(1) == ord(' '):
		break

out.release()

cv2.destroyAllWindows()
