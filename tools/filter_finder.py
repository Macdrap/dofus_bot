import cv2 as cv
from color_recognition.windowcapture import WindowCapture
from color_recognition.vision import Vision

# initialize the WindowCapture class
wincap = WindowCapture()            # ADD THE WINDOW NAME
# initialize the Vision class
vision = Vision("/assets/monstres/Astrub/Contours d'Astrub/Piou bleu.jpg")
vision.init_control_gui()

while True:
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    processed_image = vision.apply_hsv_filter(screenshot)
    # display the processed image
    cv.imshow('Matches', processed_image)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
