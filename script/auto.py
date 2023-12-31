import sys
import time
import pyautogui
import PySimpleGUI as sg
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pyautogui.useImageNotFoundException()


def quest(max_orbs, cont):
    orbs_used = 0
    while True:
        try:
            start_quest = pyautogui.locateCenterOnScreen(
                resource_path("start_quest.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            start_quest = None
        try:
            retry = pyautogui.locateCenterOnScreen(
                resource_path("retry.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            retry = None
        try:
            tap_screen = pyautogui.locateCenterOnScreen(
                resource_path("tap_screen.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            tap_screen = None
        try:
            close = pyautogui.locateCenterOnScreen(
                resource_path("close.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            close = None
        try:
            purchase = pyautogui.locateCenterOnScreen(
                resource_path("purchase.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            purchase = None
        try:
            result_screen = pyautogui.locateCenterOnScreen(
                resource_path("result_screen.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            result_screen = None
        try:
            continues = pyautogui.locateCenterOnScreen(
                resource_path("continue.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            continues = None
        try:
            buying = pyautogui.locateCenterOnScreen(
                resource_path("buying.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            buying = None
        try:
            cancel = pyautogui.locateCenterOnScreen(
                resource_path("cancel.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            cancel = None
        try:
            auto = pyautogui.locateCenterOnScreen(
                resource_path("auto.png"), confidence=0.95
            )
        except pyautogui.ImageNotFoundException:
            auto = None
        if purchase != None and buying != None and max_orbs != -1:
            if orbs_used + 5 > max_orbs:
                return "Finished"
            orbs_used += 5
            pyautogui.click(purchase)
        elif max_orbs == -1 and cancel != None and purchase != None:
            pyautogui.click(cancel)
            time.sleep(720)
        elif start_quest != None:
            pyautogui.click(start_quest)
        elif retry != None:
            pyautogui.click(retry)
        elif tap_screen != None:
            pyautogui.click(tap_screen)
        elif close != None:
            pyautogui.click(close)
        elif result_screen != None:
            pyautogui.click(result_screen)
        elif continues != None and cont:
            pyautogui.click(continues)
        elif auto != None:
            pyautogui.click(auto)


def checkTickets():
    while True:
        try:
            close = pyautogui.locateCenterOnScreen(
                resource_path("close.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            close = None
        try:
            gift = pyautogui.locateCenterOnScreen(
                resource_path("gift.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            gift = None
        try:
            start_coop = pyautogui.locateCenterOnScreen(
                resource_path("start_coop.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            start_coop = None
        try:
            not_enough_members = pyautogui.locateCenterOnScreen(
                resource_path("not_enough_members.png")
            )
        except pyautogui.ImageNotFoundException:
            not_enough_members = None
        try:
            purchase = pyautogui.locateCenterOnScreen(
                resource_path("buying.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            purchase = None
        if purchase != None:
            return
        if close != None and gift != None:
            pyautogui.click(close)
            time.sleep(720)
        elif not_enough_members != None and close != None:
            pyautogui.click(close)
            return
        elif start_coop != None:
            pyautogui.click(start_coop)


def coop(max_orbs, cont):
    orbs_used = 0
    while True:
        try:
            continues = pyautogui.locateCenterOnScreen(
                resource_path("continue.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            continues = None
        try:
            tap_here_screen = pyautogui.locateCenterOnScreen(
                resource_path("tap_here_to_continue.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            tap_here_screen = None
        try:
            create_room = pyautogui.locateCenterOnScreen(
                resource_path("create_room.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            create_room = None
        try:
            public = pyautogui.locateCenterOnScreen(
                resource_path("public.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            public = None
        try:
            open_slot = pyautogui.locateCenterOnScreen(
                resource_path("slot.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            open_slot = None
        try:
            retry = pyautogui.locateCenterOnScreen(
                resource_path("retry.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            retry = None
        try:
            auto = pyautogui.locateCenterOnScreen(
                resource_path("auto.png"), confidence=0.95
            )
        except pyautogui.ImageNotFoundException:
            auto = None
        try:
            start_coop = pyautogui.locateCenterOnScreen(
                resource_path("start_coop.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            start_coop = None
        try:
            confirm = pyautogui.locateCenterOnScreen(
                resource_path("confirm.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            confirm = None
        try:
            not_enough_members = pyautogui.locateCenterOnScreen(
                resource_path("not_enough_members.png")
            )
        except pyautogui.ImageNotFoundException:
            not_enough_members = None
        try:
            tap_screen = pyautogui.locateCenterOnScreen(
                resource_path("tap_screen.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            tap_screen = None
        try:
            result_screen = pyautogui.locateCenterOnScreen(
                resource_path("result_screen.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            result_screen = None
        try:
            players_not_ready = pyautogui.locateCenterOnScreen(
                resource_path("players_not_ready.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            players_not_ready = None
        try:
            purchase = pyautogui.locateCenterOnScreen(
                resource_path("purchase.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            purchase = None
        try:
            assist_point = pyautogui.locateCenterOnScreen(
                resource_path("assist_point.png"), confidence=0.8
            )
        except pyautogui.ImageNotFoundException:
            assist_point = None
        if purchase != None and create_room != None and max_orbs != -1:
            if orbs_used + 1 > max_orbs:
                return "Finished"
            pyautogui.click(create_room)
            orbs_used += 1
        elif max_orbs == -1 and purchase != None:
            cancel = None
            while cancel == None:
                cancel = pyautogui.locateCenterOnScreen(
                    resource_path("cancel.png"), confidence=0.8
                )
            pyautogui.click(cancel)
            time.sleep(720)
        elif create_room != None:
            pyautogui.click(create_room)
            checkTickets()
        elif not_enough_members != None:
            close = None
            while close == None:
                close = pyautogui.locateCenterOnScreen(
                    resource_path("close.png"), confidence=0.8
                )
            pyautogui.click(close)
        elif players_not_ready != None:
            cancel = None
            while cancel == None:
                cancel = pyautogui.locateCenterOnScreen(
                    resource_path("cancel.png"), confidence=0.8
                )
            pyautogui.click(cancel)
        elif public != None:
            pyautogui.click(public)
        elif open_slot == None and start_coop != None and public == None:
            pyautogui.click(start_coop)
        elif retry != None:
            pyautogui.click(retry)
        elif tap_here_screen != None:
            pyautogui.click(tap_here_screen)
        elif continues != None and cont:
            pyautogui.click(continues)
        elif auto != None:
            pyautogui.click(auto)
        elif confirm != None:
            pyautogui.click(confirm)
        elif tap_screen != None:
            pyautogui.click(tap_screen)
        elif result_screen != None:
            pyautogui.click(result_screen)
        elif assist_point != None:
            close = None
            while close == None:
                close = pyautogui.locateCenterOnScreen(
                    resource_path("close.png"), confidence=0.8
                )
            pyautogui.click(close)


sg.theme("LightGreen2")

start_layout = [
    [sg.Text("Welcome to BBS Auto Farm!", font=("Helvetica", 15))],
    [
        sg.Text("Which Event type would you like to farm?", font=("Helvetica", 10)),
    ],
    [sg.Button("Quest"), sg.Button("Co-op")],
]

quest_layout_orbs = [
    [sg.Text("Welcome to BBS Auto Farm!", font=("Helvetica", 15))],
    [
        sg.Text(
            "What is the maximum amount of orbs you want to spend?",
            font=("Helvetica", 10),
        ),
    ],
    [sg.Text("(enter -1 if you want to wait for tickets to recharge)")],
    [sg.InputText(), sg.Button("Next", key="quest_orbs_next")],
    [sg.Button("Back", key="quest_orbs_back")],
]

quest_layout_cont = [
    [sg.Text("Welcome to BBS Auto Farm!", font=("Helvetica", 15))],
    [
        sg.Text("Would you like to use revival candles?", font=("Helvetica", 10)),
        sg.Button("Yes", key="quest_cont_yes"),
        sg.Button("No", key="quest_cont_no"),
    ],
    [sg.Button("Back", key="quest_cont_back")],
]

coop_layout_orbs = [
    [sg.Text("Welcome to BBS Auto Farm!", font=("Helvetica", 15))],
    [
        sg.Text(
            "What is the maximum amount of orbs you want to spend?",
            font=("Helvetica", 10),
        ),
    ],
    [sg.Text("(enter -1 if you want to wait for tickets to recharge)")],
    [sg.InputText(), sg.Button("Next", key="coop_orbs_next")],
    [sg.Button("Back", key="coop_orbs_back")],
]

coop_layout_cont = [
    [sg.Text("Welcome to BBS Auto Farm!", font=("Helvetica", 15))],
    [
        sg.Text("Would you like to use revival candles?", font=("Helvetica", 10)),
        sg.Button("Yes", key="coop_cont_yes"),
        sg.Button("No", key="coop_cont_no"),
    ],
    [sg.Button("Back", key="coop_cont_back")],
]

running_layout = [
    [sg.Text("Thanks for using to BBS Auto Farm!", font=("Helvetica", 15))],
    [sg.Text("Place BBS in view and let the magic happen!", font=("Helvetica", 15))],
    [
        sg.Text(
            "Close this window when you want to start",
            font=("Helvetica", 15),
        ),
    ],
    [sg.Text("To stop press Ctrl+C in the terminal", font=("Helvetica", 15))],
]

orbs = 0
play_quest = True
play_coop = False

layout = (
    [
        [
            sg.Column(start_layout, key="start_layout"),
            sg.Column(quest_layout_orbs, visible=False, key="quest_layout_orbs"),
            sg.Column(quest_layout_cont, visible=False, key="quest_layout_cont"),
            sg.Column(coop_layout_cont, visible=False, key="coop_layout_cont"),
            sg.Column(running_layout, visible=False, key="running_layout"),
            sg.Column(coop_layout_orbs, visible=False, key="coop_layout_orbs"),
        ]
    ],
)

window = sg.Window(
    "BBS Auto Farm",
    layout,
    element_justification="c",
    margins=(100, 50),
)

current_layout = "start_layout"
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "Quest":
        play_quest = True
        window[current_layout].update(visible=False)
        window["quest_layout_orbs"].update(visible=True)
        current_layout = "quest_layout_orbs"
    elif event == "Co-op":
        play_coop = True
        window[current_layout].update(visible=False)
        window["coop_layout_orbs"].update(visible=True)
        current_layout = "coop_layout_orbs"
    elif event == "quest_orbs_next":
        orbs = int(values[0])
        window[current_layout].update(visible=False)
        window["quest_layout_cont"].update(visible=True)
        current_layout = "quest_layout_cont"
    elif event == "quest_orbs_back":
        orbs = 0
        window[current_layout].update(visible=False)
        window["start_layout"].update(visible=True)
        current_layout = "start_layout"
    elif event == "quest_cont_back":
        window[current_layout].update(visible=False)
        window["quest_layout_orbs"].update(visible=True)
        current_layout = "quest_layout_orbs"
    elif event == "coop_cont_back":
        window[current_layout].update(visible=False)
        window["start_layout"].update(visible=True)
        current_layout = "start_layout"
    elif event == "coop_cont_yes":
        cont = True
        window[current_layout].update(visible=False)
        window["running_layout"].update(visible=True)
        current_layout = "running_layout"
    elif event == "coop_cont_no":
        cont = False
        window[current_layout].update(visible=False)
        window["running_layout"].update(visible=True)
        current_layout = "running_layout"
    elif event == "quest_cont_yes":
        cont = True
        window[current_layout].update(visible=False)
        window["running_layout"].update(visible=True)
        current_layout = "running_layout"
    elif event == "quest_cont_no":
        cont = False
        window[current_layout].update(visible=False)
        window["running_layout"].update(visible=True)
        current_layout = "running_layout"
    elif event == "coop_orbs_back":
        orbs = 0
        window[current_layout].update(visible=False)
        window["start_layout"].update(visible=True)
        current_layout = "start_layout"
    elif event == "coop_orbs_next":
        orbs = int(values[1])
        window[current_layout].update(visible=False)
        window["coop_layout_cont"].update(visible=True)
        current_layout = "coop_layout_cont"
    elif event == "coop_cont_back":
        window[current_layout].update(visible=False)
        window["coop_layout_orbs"].update(visible=True)
        current_layout = "coop_layout_orbs"

window.close()
print("Press Ctrl+C or close this window to stop BBS Auto Farm")
cont = False
try:
    if play_quest:
        print(quest(orbs, cont))
    elif play_coop:
        print(coop(orbs, cont))
except KeyboardInterrupt as k:
    print("Stopped")
    print("Thanks for using BBS Auto Farm!")
    print("Closing")
    time.sleep(5)
except Exception as e:
    print(e)
    time.sleep(100)
