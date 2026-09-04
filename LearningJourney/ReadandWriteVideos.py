import numpy
import cv2

def ShowMyCamera(): # create a function to show the main camera
    cap = cv2.VideoCapture(0) # make a variable with the value of the main camera
    while True: # create an infinite loop
        ret, frame = cap.read() # read the frames coming from the camera

        if ret: # if the frame was read successfully:
            cv2.imshow("my first video", frame) # show the frame thats coming from the camera
            key = cv2.waitKey(1) # adjust the refresh rate to 1/1000
        if key == ord('a'): # if the key 'a' has pressed break the process
            break
        
    cap.release()
    cv2.destroyAllWindows()

# __________________________________________________________________________

def ReadvideoFromFile(): # creating a function to read a video from a file
    cap = cv2.VideoCapture(r'D:\current system\Python\firstone\Opencv\Tests\Ressources\Videos\myfirstopencvvideo.avi') # make a variable with the value of the video file
    while True: # create an infinite loop
        ret, frame = cap.read() # read the frames from the video
        if ret: # if the frame was read successfully
            cv2.imshow("Read Video", frame) # show the frame coming from the video

        delay = int(1000/60) # calculate the delay to get 60 frames per second
        if cv2.waitKey(delay) == ord('q'): # if the 'q' key is pressed break the loop
            break

    cap.release()
    cv2.destroyAllWindows()

# __________________________________________________________________________

def WriteVideoToFile():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    outPath = (r'D:\current system\Python\firstone\Opencv\Tests\Ressources\Videos\myfirstopencvvideo.avi')

    out = cv2.VideoWriter(outPath, fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow("Raisky", frame)
            if cv2.waitKey(int(1000/60)) == ord('q'):
                break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

#ShowMyCamera()
#ReadvideoFromFile()
WriteVideoToFile()