import pynput,time

def mouse_simulator():

    # 读鼠标坐标
    controller = pynput.mouse.Controller()
    print('The current pointer position is {0}'.format(controller.position))
    # 定位鼠标的绝对坐标
    # controller.position = (x,y)
    # print('Now we have moved it to {0}'.format(controller.position))
    # 按下鼠标左键
    controller.press(pynput.mouse.Button.left)  # 按住鼠标左键

    time.sleep(0.05)

    # 移动鼠标到相对位置
    controller.move(100, 100)

    controller.scroll(0, -200)

    time.sleep(0.05)

    # 放开鼠标
    controller.release(pynput.mouse.Button.left)      # 放开鼠标左键

    # 双击鼠标
    # controller.click(pynput.mouse.Button.left, 2)     # 点击鼠标2下

    # 鼠标滚轮 dx,dy
    # controller.scroll(0, -200)              # 滚动鼠标

def clicker(num):
    controller=pynput.mouse.Controller()
    # controller.click(pynput.mouse.Button.left,num)
    for i in range(num):
        controller.press(pynput.mouse.Button.left)
        time.sleep(0.1)
        controller.release(pynput.mouse.Button.left)

time.sleep(4)
clicker(100)


'''
另一种写法
    # for i in range(1):
        # controller.press(pynput.mouse.Button.left)        # 按住鼠标左键
        # controller.release(pynput.mouse.Button.left)      # 放开鼠标左键
        # time.sleep(0.1)
        # controller.press(pynput.mouse.Button.right,1)        # 按住鼠标右键
        # controller.release(pynput.mouse.Button.right)      # 放开鼠标右键
        # time.sleep(0.1)


'''