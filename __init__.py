#! python3
import pyautogui, time, random
print('Press Ctrl-C to quit.')

def mouse_position(x,y):
    pyautogui.moveTo(x, y)
    atual_position = f'\nPosition: X:{x} | Y:{y}'
    print(atual_position)
    print('Application is running!')
    time.sleep(15)

try:
    while True:
        x = random.randint(500, 1098)
        y = random.randint(100, 500)
        mouse_position(x, y)

except KeyboardInterrupt:
    print('\n')
