import pyautogui as gui
import time


class Map:

    def __init__(self):
        self.current_map_index = 0

    def loop_around(self, loop_coordinates):
        if self.current_map_index == len(loop_coordinates):
            self.current_map_index = 0
        x = loop_coordinates[self.current_map_index][0]
        y = loop_coordinates[self.current_map_index][1]
        gui.moveTo(x, y)
        time.sleep(0.3)
        gui.leftClick()
        time.sleep(3)
        self.current_map_index += 1
