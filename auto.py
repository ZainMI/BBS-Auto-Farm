import time
import pyautogui
import PySimpleGUI as sg


def quest(max_orbs, cont):
    orbs_used = 0
    while True:
        cancelTimer = False
        start_quest = pyautogui.locateOnScreen("start_quest.png", confidence=0.8)
        retry = pyautogui.locateOnScreen("retry.png", confidence=0.8)
        tap_screen = pyautogui.locateOnScreen("tap_screen.png", confidence=0.8)
        close = pyautogui.locateOnScreen("close.png", confidence=0.8)
        purchase = pyautogui.locateOnScreen("purchase.png", confidence=0.8)
        result_screen = pyautogui.locateOnScreen("result_screen.png", confidence=0.8)
        continues = pyautogui.locateOnScreen("continue.png", confidence=0.8)
        buying = pyautogui.locateOnScreen("buying.png", confidence=0.8)
        cancel = pyautogui.locateOnScreen("cancel.png", confidence=0.8)
        auto = pyautogui.locateOnScreen("auto.png", confidence=0.95)
        if purchase != None and buying != None and max_orbs != -1:
            if orbs_used + 5 > max_orbs:
                return "Finished"
            orbs_used += 5
            pyautogui.click(pyautogui.center(purchase))
        if max_orbs == -1 and cancel != None and purchase != None:
            pyautogui.click(pyautogui.center(cancel))
            cancelTimer = True
        elif start_quest != None:
            pyautogui.click(pyautogui.center(start_quest))
        elif retry != None:
            pyautogui.click(pyautogui.center(retry))
        elif tap_screen != None:
            pyautogui.click(pyautogui.center(tap_screen))
        elif close != None:
            pyautogui.click(pyautogui.center(close))
        elif result_screen != None:
            pyautogui.click(pyautogui.center(result_screen))
        elif continues != None and cont:
            pyautogui.click(pyautogui.center(continues))
        elif auto != None:
            pyautogui.click(pyautogui.center(auto))

        if cancelTimer:
            time.sleep(720)


def coop(cont):
    while True:
        create_room = pyautogui.locateOnScreen("create_room.png", confidence=0.8)
        public = pyautogui.locateOnScreen("public.png", confidence=0.8)
        last_player = pyautogui.locateOnScreen("last_player.png", confidence=0.8)
        tap_screen = pyautogui.locateOnScreen(
            "tap_here_to_continue.png", confidence=0.8
        )
        retry = pyautogui.locateOnScreen("retry.png", confidence=0.8)
        auto = pyautogui.locateOnScreen("auto.png", confidence=0.95)
        continues = pyautogui.locateOnScreen("continue.png", confidence=0.8)
        start_coop = pyautogui.locateOnScreen("start_coop.png", confidence=0.8)
        confirm = pyautogui.locateOnScreen("confirm.png", confidence=0.8)
        if create_room != None:
            pyautogui.click(pyautogui.center(create_room))
        elif public != None:
            pyautogui.click(pyautogui.center(public))
        elif last_player == None and start_coop != None and public == None:
            pyautogui.click(pyautogui.center(start_coop))
        elif retry != None:
            pyautogui.click(pyautogui.center(retry))
        elif tap_screen != None:
            pyautogui.click(pyautogui.center(tap_screen))
        elif continues != None and cont:
            pyautogui.click(pyautogui.center(continues))
        elif auto != None:
            pyautogui.click(pyautogui.center(auto))
        elif confirm != None:
            pyautogui.click(pyautogui.center(confirm))


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
    [sg.InputText(), sg.Button("Next")],
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
        window["coop_layout_cont"].update(visible=True)
        current_layout = "coop_layout_cont"
    elif event == "Next":
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

window.close()
print("Press Ctrl+C to stop")

try:
    if play_quest:
        print(quest(orbs, cont))
    elif play_coop:
        print(coop(cont))
except:
    print("Stopped")
