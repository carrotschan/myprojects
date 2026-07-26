'''
LIBRARIES USED:
1. numpy
2. cv2
3. random
'''
import numpy as np
import cv2
import random
##Functions
def get_random_rgb():
    # Generate a random RGB color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def fun(event, x, y, flags, user):
    '''
    Mouse callback function to handle drawing shapes on the canvas based on mouse events.
    '''
    global ix, iy, drawing, f1, color, shape, twoclick
   
    if event == cv2.EVENT_LBUTTONDOWN and shape == "circle": # Left Click
        drawing = True
        cv2.circle(f1, (x,y), 20, color, -1)
    elif event == cv2.EVENT_LBUTTONDOWN and shape == "rect" and twoclick == False: # Left Click
        ix, iy = x, y
        drawing = True
        twoclick = True
    elif event == cv2.EVENT_LBUTTONDOWN and shape == "rect" and twoclick == True:
            cv2.rectangle(f1, (ix, iy), (x,y), color, 20)

    elif event == cv2.EVENT_FLAG_RBUTTON:
        color = get_random_rgb()
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode == 'brush':
                cv2.circle(f1, (x, y), 10, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

#Setting up the canvas and initial parameters
f1 = np.full((500,500,3), 255, dtype=np.uint8)
ix, iy = -1, -1
drawing = False
shape = "circle"
mode = 'brush' 
twoclick = False
color = get_random_rgb()

#Creating a window and attaching the mouse callback function
cv2.namedWindow("b1", cv2.WINDOW_FREERATIO)
cv2.setMouseCallback("b1", fun)



c = 0

#Main Loop
while True:
    cv2.imshow("b1", f1)
    print(shape)
    key = cv2.waitKey(1)

    if key == ord("q"): #Quit
        break
    elif key ==ord("s"):
        cv2.imwrite(f"output_{c}.jpg".format(c), f1)
        c += 1
        print("Image Saved")
    elif key == ord('r'):
        shape = "rect"
    elif key == ord('c'):
        shape = "circle"
cv2.destroyAllWindows()