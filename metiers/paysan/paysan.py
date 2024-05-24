import pyautogui as gui
import time
from color_recognition.windowcapture import WindowCapture
from color_recognition.vision import Vision
from movement.road import paysan_road_1
from movement.map import Map
from assets.absolute_path import ble_absolute_path, current_map_absolute_path

paysan_loop_1 = Map()
wincap = WindowCapture("BlueStacks App Player 1")
vision = Vision(ble_absolute_path)
img = gui.screenshot(region=(125, 97, 50, 20)) ## ADD A SCREEN RESOLUTION AND GET THE DETAILS FOR COORDINATES FROM ACTUAL SIZE. RECORD IT IN A FILE SCREEEN SIZE -LATER STAGE REPLACE GUI BY WINCREENSHOT
img.save(current_map_absolute_path)
current_map_vision = Vision(current_map_absolute_path)
has_map_been_recolted = False

while True:
    screenshot = wincap.get_screenshot()
    found = current_map_vision.find(screenshot, 0.9)
    found_objects = vision.find(screenshot, 0.45)

    while has_map_been_recolted is False:
        for found_object in found_objects:
            gui.moveTo(found_object[0] + 150, found_object[1] + 40)
            time.sleep(0.3)
            gui.leftClick()
        time.sleep(3)
        paysan_loop_1.loop_around(paysan_road_1)
        has_map_been_recolted = True

    if len(found) == 0:
        time.sleep(3)
        img = gui.screenshot(region=(125, 97, 50, 20))
        img.save("C://Users//44739//PycharmProjects//dofus_touch_bot//assets//images//current_map.jpg")
        current_map_vision = Vision(
            "C://Users//44739//PycharmProjects//dofus_touch_bot//assets//images//current_map.jpg")
        has_map_been_recolted = False
