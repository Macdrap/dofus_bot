import cv2 as cv
from color_recognition.windowcapture import WindowCapture
from color_recognition.vision import Vision



# initialize the WindowCapture class
wincap = WindowCapture("BlueStacks App Player 1")            # ADD THE WINDOW NAME
# initialize the Vision class
vision = Vision("C://Users//44739//PycharmProjects//dofus_touch_bot//assets//images//current_map.jpg")
while True:
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    rectangles = vision.find(screenshot, 0.9)
    print(len(rectangles))
    # draw the detection results onto the original image
    detection_image = vision.draw_rectangles(screenshot, rectangles)
    # display the processed image
    cv.imshow('Matches', detection_image)

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(0) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
