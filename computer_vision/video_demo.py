import cv2
import numpy as np
import os

def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"Video file is not found \n{path_of_video}")
        return None
    video=cv2.VideoCapture(path_of_video)
    while True:
        status, frame= video.read()
        if not status:
            print("Video could not be read!!!")
            break
        cv2.imshow("Video",frame)
        if cv2.waitKey(1)== ord('q'):    #1 represents 1 millisecond
            break
    # Clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    videofile=r"C:\Users\aditi\Downloads\pexels_videos_2759477 (2160p).mp4"    #r - raw string is just a string without any power
    load_video(videofile)