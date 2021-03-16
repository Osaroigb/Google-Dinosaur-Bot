# import required modules
from PIL import ImageOps, ImageGrab
from time import sleep
import numpy as np
import pyautogui


class Coordinates:

    # coordinates of replay button to start the game
    replay_button = (360, 214)

    # this coordinates represent the top-right coordinates
    # that will be used to define the front box
    dinosaur = (149, 239)


def restart_game():

    # using pyautogui library, we are clicking on the
    # replay button without any user interaction
    pyautogui.click(Coordinates.replay_button)

    # we will keep our Bot always down that
    # will prevent him to get hit by bird
    pyautogui.keyDown("down")


def press_space():

    # releasing the Down Key
    pyautogui.keyUp("down")

    # pressing Space to overcome Bush
    pyautogui.keyDown("space")

    # so that Space Key will be recognized easily
    sleep(0.05)

    # printing the "Jump" statement on the
    # terminal to see the current output
    print("jump")
    sleep(0.10)

    # releasing the Space Key
    pyautogui.keyUp("space")

    # again pressing the Down Key to keep my Bot always down
    pyautogui.keyDown("down")


def image_grab():

    # defining the coordinates of box in front of dinosaur
    box = (Coordinates.dinosaur[0] + 30, Coordinates.dinosaur[1],
           Coordinates.dinosaur[0] + 120, Coordinates.dinosaur[1] + 2)

    # grabbing all the pixels values in form of RGB tuples
    image = ImageGrab.grab(bbox=box)

    # converting RGB to Grayscale to
    # make processing easy and result faster
    gray_image = ImageOps.grayscale(image)

    # using numpy to get sum of all grayscale pixels
    a = np.array(gray_image.getcolors())

    # returning the sum
    print(a.sum())
    return a.sum()


print("Hey.. Dino game about to start in 5 seconds")
sleep(5)

# function to restart the game
restart_game()

while True:

    # 435 is the sum of white pixels values of box.
    # You may get different value is you are taking bigger
    # or smaller box than the box taken in this article.
    # if value returned by "imageGrab" function is not equal to 435,
    # it means either bird or bush is coming towards dinosaur
    if image_grab() != 435:

        press_space()

        # time to recognize the operation performed by above function
        sleep(0.1)
