import pynput,time

controler = pynput.keyboard.Controller()

def command(cmdlist):

    for cmd in cmdlist:
        controler.press('t')
        controler.release('t')

        time.sleep(0.05)
        controler.type(cmd)
        time.sleep(0.05)

        controler.press(pynput.keyboard.Key.enter)
        controler.release(pynput.keyboard.Key.enter)
        time.sleep(0.1*len(cmdlist))

# time.sleep(3)
# longlist=['/summon ender_dragon ~ ~ ~ {DragonPhase:0}','/summon ender_dragon ~ ~ ~ {DragonPhase:1}','/summon ender_dragon ~ ~ ~ {DragonPhase:2}',
#          "/summon ender_dragon ~ ~ ~ {DragonPhase:3}",'/summon ender_dragon ~ ~ ~ {DragonPhase:4}','/summon ender_dragon ~ ~ ~ {DragonPhase:5}']
# shortcomd=['/summon ender_dragon ~ ~ ~ {DragonPhase:5}']
# command(shortcomd)

def fd(step):
    controler.press('w')
    time.sleep(step)
    controler.release('w')

time.sleep(2)
# fd(3)

#这是按下组合键的意思，指的是同时按下shift和a

with controler.pressed(pynput.keyboard.Key.shift):
    controler.press('a')
    controler.release('a')
