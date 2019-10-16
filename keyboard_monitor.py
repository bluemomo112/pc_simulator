'''
键盘监听
'''

import pynput
import time

# for i in pynput.keyboard.Key:
#     print(i)

def printname(key):
    try:
        print(key.name)
        # print(key.char)
    except:
        print(key)


lis=pynput.keyboard.Listener(on_release=printname)
lis.start()
lis.join()

# keyboardMonitor()



