
'''
鼠标监听
我的屏幕分辨率是1920 X 1080，
因此左上角是00点，右下角最大是1920,1080
一个鼠标监听器是一个线程。线程，所有的回调将从线程调用。从任何地方调用pynput.mouse.Listener.stop，
或者调用pynput.mouse.Listener.StopException或从回调中返回False来停止监听器

'''

## 监听鼠标.
from pynput.mouse import Listener

def on_move(x, y):
    # 监听鼠标移动
    print('Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    # 监听鼠标点击
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    # 监听鼠标滚轮
    print('Scrolled {0}'.format((x, y)))

def mouseMonitor():
    # 连接事件以及释放
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

mouseMonitor()