#pip install pynput
#pip install keyboard
from pynput import mouse
import keyboard
import random

#ЯЧЕЙКИ ИНВЕНТАРЯ, БЛОКИ КОТОРЫХ НАДО РАНДОМИТЬ
cells = ['1', '2', '3', '4']
#КОЭФФИЦИЕНТЫ СООТНОШЕНИЯ БЛОКОВ
factor = [1.0, 1.0, 1.0, 1.0]
const = 10
fac_cells = list(map(int, "".join([str(x)*int(factor[cells.index(x)]*const) for x in cells])))

def mouse_click(left, right, button, pressed):
    if pressed and button == mouse.Button.right:
        keyboard.press_and_release(str(fac_cells[random.randint(0, len(fac_cells)-1)]))
       
with mouse.Listener(on_click=mouse_click) as listener:
    listener.join()

