import time
import pyautogui
import PySimpleGUI as sg


def quest(max_orbs, cont):
    orbs_used = 0
    while True:
        start_quest = pyautogui.locateCenterOnScreen(
            "./img/start_quest.png", confidence=0.8
        )
        retry = pyautogui.locateCenterOnScreen("./img/retry.png", confidence=0.8)
        tap_screen = pyautogui.locateCenterOnScreen(
            "./img/tap_screen.png", confidence=0.8
        )
        close = pyautogui.locateCenterOnScreen("./img/close.png", confidence=0.8)
        purchase = pyautogui.locateCenterOnScreen("./img/purchase.png", confidence=0.8)
        result_screen = pyautogui.locateCenterOnScreen(
            "./img/result_screen.png", confidence=0.8
        )
        continues = pyautogui.locateCenterOnScreen("./img/continue.png", confidence=0.8)
        buying = pyautogui.locateCenterOnScreen("./img/buying.png", confidence=0.8)
        cancel = pyautogui.locateCenterOnScreen("./img/cancel.png", confidence=0.8)
        auto = pyautogui.locateCenterOnScreen("./img/auto.png", confidence=0.95)
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
        close = pyautogui.locateCenterOnScreen("./img/close.png", confidence=0.8)
        gift = pyautogui.locateCenterOnScreen("./img/gift.png", confidence=0.8)
        start_coop = pyautogui.locateCenterOnScreen(
            "./img/start_coop.png", confidence=0.8
        )
        not_enough_members = pyautogui.locateCenterOnScreen(
            "./img/not_enough_members.png"
        )
        purchase = pyautogui.locateCenterOnScreen("./img/buying.png", confidence=0.8)
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
    death_time = None
    while True:
        continues = pyautogui.locateCenterOnScreen("./img/continue.png", confidence=0.8)
        tap_here_screen = pyautogui.locateCenterOnScreen(
            "./img/tap_here_to_continue.png", confidence=0.8
        )
        if death_time != None and time.time() - death_time > 300 and continues != None:
            death_time = None
            pyautogui.click(continues)
            continue
        elif tap_here_screen != None:
            pyautogui.click(tap_here_screen)
            continue
        elif death_time != None and time.time() - death_time < 300:
            continue
        create_room = pyautogui.locateCenterOnScreen(
            "./img/create_room.png", confidence=0.8
        )
        public = pyautogui.locateCenterOnScreen("./img/public.png", confidence=0.8)
        open_slot = pyautogui.locateCenterOnScreen("./img/slot.png", confidence=0.8)
        retry = pyautogui.locateCenterOnScreen("./img/retry.png", confidence=0.8)
        auto = pyautogui.locateCenterOnScreen("./img/auto.png", confidence=0.95)
        start_coop = pyautogui.locateCenterOnScreen(
            "./img/start_coop.png", confidence=0.8
        )
        confirm = pyautogui.locateCenterOnScreen("./img/confirm.png", confidence=0.8)
        not_enough_members = pyautogui.locateCenterOnScreen(
            "./img/not_enough_members.png"
        )
        tap_screen = pyautogui.locateCenterOnScreen(
            "./img/tap_screen.png", confidence=0.8
        )
        result_screen = pyautogui.locateCenterOnScreen(
            "./img/result_screen.png", confidence=0.8
        )
        players_not_ready = pyautogui.locateCenterOnScreen(
            "./img/players_not_ready.png", confidence=0.8
        )
        purchase = pyautogui.locateCenterOnScreen("./img/buying.png", confidence=0.8)

        if purchase != None and create_room != None and max_orbs != -1:
            if orbs_used + 1 > max_orbs:
                return "Finished"
            pyautogui.click(create_room)
            orbs_used += 1
        elif max_orbs == -1 and purchase != None:
            cancel = None
            while cancel == None:
                cancel = pyautogui.locateCenterOnScreen(
                    "./img/cancel.png", confidence=0.8
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
                    "./img/close.png", confidence=0.8
                )
            pyautogui.click(close)
        elif players_not_ready != None:
            cancel = None
            while cancel == None:
                cancel = pyautogui.locateCenterOnScreen(
                    "./img/cancel.png", confidence=0.8
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
        elif continues != None and not cont:
            death_time = time.time()
        elif auto != None:
            pyautogui.click(auto)
        elif confirm != None:
            pyautogui.click(confirm)
        elif tap_screen != None:
            pyautogui.click(tap_screen)
        elif result_screen != None:
            pyautogui.click(result_screen)


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
play_quest = False
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
print("Press Ctrl+C or close this window to stop")

try:
    if play_quest:
        print(quest(orbs, cont))
    elif play_coop:
        print(coop(orbs, cont))
except KeyboardInterrupt as k:
    print("Stopped")
    print("Thanks for using BBS Auto Farm!")
    time.sleep(5)
except Exception as e:
    print(e)
    time.sleep(100)
