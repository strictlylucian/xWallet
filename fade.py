from dearpygui.core import *
from dearpygui.simple import *
from colors import *
import time
import threading


def separator_fade(separator):
    n = range(102, -2, -10)
    for i in n:
        set_item_color(separator, mvGuiCol_Separator, [0, 0, 0, i])
        time.sleep(0.000005)


def button_fade(button):
    if Status.lightmode:
        n = range(102, 30, -10)
        for i in n:
            set_item_color(button, mvGuiCol_Button, [255, 255, 255, i])
            time.sleep(0.000005)
    else:
        n = range(102, 30, -10)
        for i in n:
            set_item_color(button, mvGuiCol_Button, [57, 56, 56, i])
            time.sleep(0.000005)

def child_fade(child):
    if Status.lightmode:
        n = range(255, -2, -3)
        for i in n:
            set_item_color(child, mvGuiCol_ChildBg, [255, 255, 255, i])
            time.sleep(0.000005)
    else:
        n = range(255, -2, -3)
        for i in n:
            set_item_color(child, mvGuiCol_Button, [11, 11, 11, i])
            time.sleep(0.000005)

def text_fade(text):
    if Status.lightmode:
        n = range(255, -2, -2)
        for i in n:
            set_item_color(text, mvGuiCol_Text, [0, 0, 0, i])
            time.sleep(0.000005)
    else:
        n = range(255, -2, -2)
        for i in n:
            set_item_color(text, mvGuiCol_Text, [255, 255, 255, i])
            time.sleep(0.000005)

def border_fade(border):
    if Status.lightmode:
        n = range(128, -2, -10)
        for i in n:
            set_item_color(border, mvGuiCol_Border, [192, 190, 190, i])
    else:
        n = range(128, -2, -10)
        for i in n:
            set_item_color(border, mvGuiCol_Border, [0, 0, 0, i])

def frame_fade(frame):
    if Status.lightmode:
        n = range(255, -2, -5)
        for i in n:
            set_item_color(frame, mvGuiCol_FrameBg, [255, 255, 255, i])
            time.sleep(0.000005)
    else:
        n = range(255, -2, -5)
        for i in n:
            set_item_color(frame, mvGuiCol_FrameBg, [33, 30, 30, i])
            time.sleep(0.000005)


def fade_out(data):
    config = get_item_children(data)
    for i in config:
        x  = get_item_type(i)
        if x == "mvAppItemType::Group":
            threading.Thread(target=border_fade(i)).start()
            threading.Thread(target=separator_fade(i)).start()
            threading.Thread(target=frame_fade(i)).start()
            threading.Thread(target=text_fade(i)).start()
            threading.Thread(target=child_fade(i)).start()
            threading.Thread(target=button_fade(i)).start()
        if does_item_exist("exchange_logo"):
            clear_drawing("exchange_logo")
        else:
            pass
        if does_item_exist("Plot"):
            delete_item("Plot")
        else:
            pass
        if does_item_exist("PlotDOGE"):
            delete_item("PlotDOGE")
        else:
            pass

def fade_in(data):
    config = get_item_children(data)
    for i in config:
        x  = get_item_type(i)
        if x == "mvAppItemType::Group":
            threading.Thread(target=border_fade_in(i)).start()
            threading.Thread(target=separator_fade_in(i)).start()
            threading.Thread(target=frame_fade_in(i)).start()
            threading.Thread(target=text_fade_in(i)).start()
            threading.Thread(target=child_fade_in(i)).start()
            threading.Thread(target=button_fade_in(i)).start()


def separator_fade_in(separator):
    n = range(0, 103, 10)
    for i in n:
        set_item_color(separator, mvGuiCol_Separator, [0, 0, 0, i])
        time.sleep(0.000005)


def button_fade_in(button):
    if Status.lightmode:
        n = range(0, 103, 10)
        for i in n:
            set_item_color(button, mvGuiCol_Button, [255, 255, 255, i])
            time.sleep(0.000005)
    else:
        n = range(0, 103, 10)
        for i in n:
            set_item_color(button, mvGuiCol_Button, [57, 56, 56, i])
            time.sleep(0.000005)

def child_fade_in(child):
    if Status.lightmode:
        n = range(0, 256, 2)
        for i in n:
            set_item_color(child, mvGuiCol_ChildBg, [255, 255, 255, i])
            time.sleep(0.000005)
    else:
        n = range(0, 256, 2)
        for i in n:
            set_item_color(child, mvGuiCol_ChildBg, [11, 11, 11, i])
            time.sleep(0.000005)

def text_fade_in(text):
    if Status.lightmode:
        n = range(0, 256, 2)
        for i in n:
            set_item_color(text, mvGuiCol_Text, [0, 0, 0, i])
            time.sleep(0.000005)
    else:
        n = range(0, 256, 2)
        for i in n:
            set_item_color(text, mvGuiCol_Text, [255, 255, 255, i])
            time.sleep(0.000005)

def border_fade_in(border):
    if Status.lightmode:
        n = range(0, 129, 10)
        for i in n:
            set_item_color(border, mvGuiCol_Border, [192, 190, 190, i])
    else:
        n = range(0, 129, 10)
        for i in n:
            set_item_color(border, mvGuiCol_Border, [0, 0, 0, i])

def frame_fade_in(frame):
    if Status.lightmode:
        n = range(0, 256, 2)
        for i in n:
            set_item_color(frame, mvGuiCol_FrameBg, [255, 255, 255, i])
            time.sleep(0.0000005)
    else:
        n = range(0, 256, 2)
        for i in n:
            set_item_color(frame, mvGuiCol_FrameBg, [33, 30, 30, i])
            time.sleep(0.0000005)
