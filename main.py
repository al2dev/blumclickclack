import cv2
import numpy as np
import pyautogui
import time
import asyncio
import threading
import os


async def capture(img, cor_x, cor_y):
    img = os.path.join(os.path.dirname(os.path.realpath(__file__)), "patterns", img)
    pattern = cv2.imread(img)
    x1, y1, width, height = 0, 0, 375, 650

    while True:
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(frame, pattern, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.75  

        if max_val > threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + pattern.shape[1], top_left[1] + pattern.shape[0])
            x, y = top_left[0], top_left[1]
            ux, uy = pyautogui.position()
            pyautogui.click(x + cor_x, y + cor_y)  
            pyautogui.moveTo(ux, uy)

        await asyncio.sleep(0.010)


def t_capture(img, cor_x, cor_y):
    img = os.path.join(os.path.dirname(os.path.realpath(__file__)), "patterns", img)
    pattern = cv2.imread(img)
    x1, y1, width, height = 0, 0, 375, 650

    while True:
        screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(frame, pattern, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        threshold = 0.75  

        if max_val > threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + pattern.shape[1], top_left[1] + pattern.shape[0])
            x, y = top_left[0], top_left[1]
            ux, uy = pyautogui.position()
            pyautogui.click(x + cor_x, y + cor_y)
            pyautogui.moveTo(ux, uy)
        time.sleep(0.010)


async def main():
    pool_loops = []
    pool_loops.append(asyncio.create_task(capture('blum_1.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_4.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_6.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_7.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_9.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_10.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_11.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_12.png', 22, 36)))

    pool_loops.append(asyncio.create_task(capture('blum_15.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_16.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_17.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_18.png', 22, 36)))
    pool_loops.append(asyncio.create_task(capture('blum_19.png', 22, 36)))

    pool_loops.append(asyncio.create_task(capture('ice_1.png', 24,44)))
    pool_loops.append(asyncio.create_task(capture('ice_3.png', 20,34)))
    await asyncio.gather(*pool_loops)


if __name__ == "__main__":
    threading.Thread(target=t_capture, args=('e_blum_22.png', 11, 14,), daemon=True).start()
    threading.Thread(target=t_capture, args=('e_blum_26.png', 11, 18,), daemon=True).start()
    threading.Thread(target=t_capture, args=('e_blum_28.png', 15, 20,), daemon=True).start()
    threading.Thread(target=t_capture, args=('e_blum_34.png', 17, 23,), daemon=True).start()
    threading.Thread(target=t_capture, args=('e_blum_36.png', 20, 23,), daemon=True).start()
    threading.Thread(target=t_capture, args=('play.png', 20, 23,), daemon=True).start()

    asyncio.run(main())
    input("press ENTER for close..")
