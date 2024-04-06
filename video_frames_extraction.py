import cv2
video = cv2.VideoCapture("C:\\Users\\mawat\\Downloads\\linkedin\\WhatsApp.mp4")

fps = video.get(cv2.CAP_PROP_FPS)
print('frames per second =',fps)

minutes = 0
seconds = 2
frame_id = int(fps*(minutes*60 + seconds))
print('frame id =',frame_id)

video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
ret, frame = video.read()

cv2.imshow('frame', frame); cv2.waitKey(0)
cv2.imwrite('my_video_frame.png', frame)