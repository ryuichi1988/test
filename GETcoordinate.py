import pyautogui, sys , time
print('Press Ctrl-C to quit.')
pyautogui.moveTo(212,157)
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr+" "+str(pyautogui.pixel(x,y)))#, end=''
        print('\b' * len(positionStr), end='', flush=True)
        time.sleep(0.3)
except KeyboardInterrupt:
    print('\n')
