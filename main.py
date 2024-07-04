import cv2
import numpy as np
import pyautogui
import time
import asyncio
import threading
import os
import multiprocessing as mp


ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


async def capture(img, cor_x, cor_y):
    global ROOT_DIR
    img = os.path.join(ROOT_DIR, img)
    pattern = cv2.imread(img)
    x1, y1, width, height = 0, 50, 375, 650

    while True:
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(frame, pattern, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.5

        if max_val > threshold:
            top_left = max_loc
            #bottom_right = (top_left[0] + pattern.shape[1], top_left[1] + pattern.shape[0])
            x, y = top_left[0], top_left[1]
            ux, uy = pyautogui.position()
            pyautogui.click(x + cor_x + x1, y + cor_y + y1)
            pyautogui.moveTo(ux, uy)

        await asyncio.sleep(0.010)


def t_capture(img, cor_x, cor_y):
    global ROOT_DIR
    img = os.path.join(ROOT_DIR, img)
    pattern = cv2.imread(img)
    x1, y1, width, height = 0, 50, 375, 650

    while True:
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(frame, pattern, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.5

        if max_val > threshold:
            top_left = max_loc
            #bottom_right = (top_left[0] + pattern.shape[1], top_left[1] + pattern.shape[0])
            x, y = top_left[0], top_left[1]
            ux, uy = pyautogui.position()
            pyautogui.click(x + cor_x + x1, y + cor_y + y1)
            pyautogui.moveTo(ux, uy)
        time.sleep(0.010)


async def asyncio_clicker(patterns):
    pool_loops = []
    for p in patterns:
        img, x, y = p
        pool_loops.append(asyncio.create_task(capture(img, int(x), int(y))))
    await asyncio.gather(*pool_loops)


def thread_clicker(patterns):
    for p in patterns:
        img, x, y = p
        threading.Thread(target=t_capture, args=(img, x, y, ), daemon=True).start()


def mp_clicker(patterns):
    for p in patterns:
        #img, x, y = p
        #mp.Process(target=t_capture, args=(img, x, y, )).start()
        mp.Process(target=process_clicker, args=(p, )).start()


def process_clicker(patterns):
    asyncio.run(asyncio_clicker(patterns))


if __name__ == "__main__":
    dataset_classic = {"blums": [('blum_1.png', 22, 36),
                                 ('blum_2.png', 22, 36),
                                 ('blum_3.png', 22, 36),
                                 ('blum_4.png', 22, 36),
                                 ('blum_5.png', 22, 36),
                                 ('blum_6.png', 22, 36),
                                 ('blum_7.png', 22, 36),
                                 ('blum_8.png', 22, 36),
                                 ('blum_9.png', 22, 36),
                                 ('blum_10.png', 22, 36),
                                 ('blum_11.png', 22, 36),
                                 ('blum_12.png', 22, 36),
                                 ('blum_13.png', 22, 36),
                                 ('blum_14.png', 22, 36),
                                 ('blum_15.png', 22, 36),
                                 ('blum_16.png', 22, 36),
                                 ('blum_17.png', 22, 36),
                                 ('blum_18.png', 22, 36),
                                 ('blum_19.png', 22, 36),
                                 ('e_blum_22.png', 11, 14),
                                 ('e_blum_26.png', 11, 18),
                                 ('e_blum_28.png', 15, 20),
                                 ('e_blum_34.png', 17, 23),
                                 ('e_blum_36.png', 20, 23)],
                       "ices": [('ice_1.png', 24, 44),
                                ('ice_3.png', 20, 34)],
                       "play": [('play.png', 0, 0)],
                       "dir": "classic"}

    dataset_colab_1 = {"blums": [('patterns\\colab_1\\0.png', 20, 30),
                                 ('patterns\\colab_1\\00.png', 20, 30),
                                 ('patterns\\colab_1\\1.png', 20, 30),
                                 ('patterns\\colab_1\\2.png', 20, 30),
                                 ('patterns\\colab_1\\3.png', 20, 30),
                                 ('patterns\\colab_1\\4.png', 20, 30),
                                 ('patterns\\colab_1\\5.png', 20, 30),
                                 ('patterns\\colab_1\\6.png', 20, 30),
                                 ('patterns\\colab_1\\7.png', 20, 30),
                                 ('patterns\\colab_1\\8.png', 20, 30),
                                 ('patterns\\colab_1\\9.png', 20, 30),
                                 ('patterns\\colab_1\\10.png', 20, 30),
                                 ('patterns\\colab_1\\11.png', 20, 30),
                                 ('patterns\\colab_1\\12.png', 20, 30),
                                 ('patterns\\colab_1\\13.png', 20, 30),
                                 ('patterns\\colab_1\\14.png', 20, 30),
                                 ('patterns\\colab_1\\22.png', 20, 30),
                                 ('patterns\\colab_1\\66.png', 20, 30),
                                 ('patterns\\colab_1\\88.png', 20, 30),
                                 ('patterns\\colab_1\\ice_1.png', 20, 30),
                                 ('patterns\\colab_1\\ice_2.png', 20, 30),
                                 ('patterns\\colab_1\\ice_3.png', 20, 30),
                                 ('patterns\\colab_1\\ice_4.png', 20, 30)
                                 ],
                       "play": [('patterns\\colab_1\\play.png', 0, 0)],
                       "dir": "colab_1"}

    dict_of_mods = {"1": dataset_classic, "2": dataset_colab_1}

    mode = input("Select number of clicker mode: \r\n\r\n1 - classic\r\n2 - colab 1\r\n\r\nvariable: ")

    # Make path to patterns
    #ROOT_DIR = os.path.join(ROOT_DIR, "patterns", dict_of_mods[mode]["dir"])

    # Run pattern blum
    # asyncio.run(asyncio_clicker(dict_of_mods[mode]["blums"]))
    pat = dict_of_mods[mode]["blums"]
    np_arr = np.array(pat)
    np_arr_arr = np.array_split(np_arr, int(len(pat)/5))
    mp_clicker(np_arr_arr)

    # Run pattern ice
    #thread_clicker(dict_of_mods[mode]["ices"])

    # Run pattern play
    thread_clicker(dict_of_mods[mode]["play"])

    #input("press ENTER for start..")
