
# 注意，需要美式键盘才行。
import binascii
import time
import pynput
import GUI


def str_gb2312(a):
    str_gb = []
    a_list = list(a)
    for i in a_list:
        a_list[a_list.index(i)] = i.encode('gb2312')
    for i in range(len(a_list)):
        str_gb.append(int(binascii.hexlify(a_list[i]), 16))
    return str_gb


def push(key):
    if key == pynput.keyboard.KeyCode.from_char('y') or key == pynput.keyboard.KeyCode.from_char('t'):
        print(key)
        return False


def simulation(str_gb):
    key = pynput.keyboard.Controller()
    for i in str_gb:
        print(i)
        key.press(pynput.keyboard.Key.alt)
        for s in str(i):
            time.sleep(0.03)
            key.press(pynput.keyboard.KeyCode.from_vk(96 + int(s)))
            time.sleep(0.02)
            key.release(pynput.keyboard.KeyCode.from_vk(96 + int(s)))
        key.release(pynput.keyboard.Key.alt)
    time.sleep(0.5)
    key.press(pynput.keyboard.Key.enter)
    time.sleep(0.1)
    key.release(pynput.keyboard.Key.enter)


if __name__ == '__main__':
    while True:
        with pynput.keyboard.Listener(on_release=push) as listener:
            listener.join()
        a = GUI.play()
        print(a)
        simulation(str_gb2312(a))
