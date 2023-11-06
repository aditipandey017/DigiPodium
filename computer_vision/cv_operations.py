import cv2
import numpy as np
import os

def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"Video file is not found \n{path_of_video}")
        return None
    video=cv2.VideoCapture(path_of_video)
    cv2.namedWindow("Video")
    cv2.createTrackbar("ksize","Video",3,100, lambda x:None)
    while True:
        status, frame= video.read()
        if not status:
            print("Video could not be read!!!")
            break
        # Operations
        # 1. resize
        frame= cv2.resize(frame,(None,None),fx=.3,fy=.3)   #half the size and none means no shape is defined
        height, width, _= frame.shape
        # 2. convert to gray scale
        # frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 3. blur
        ksize= cv2.getTrackbarPos("ksize","Video")
        try: frame= cv2.GaussianBlur(frame,(ksize,ksize),0)
        except: pass
        # 4. add text
        cv2.putText(
            frame,
            "Uncharted 4: the lost legacy",
            (width//2-200, height//2),  #coordinates/origin
            cv2.FONT_HERSHEY_SIMPLEX,   #font face
            1,  #font size
            (0,0,255),  #red color
            2   #thickness
        )
        # 5. add graphics 
        cv2.imshow("Video",frame)
        if cv2.waitKey(1)== ord('q'):    #1 represents 1 millisecond
            break
    # Clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    videofile=r"C:\Users\aditi\Downloads\pexels_videos_2759477 (2160p).mp4"    #r - raw string is just a string without any power
    load_video(videofile)