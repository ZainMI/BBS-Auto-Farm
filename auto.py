import time
import pyautogui


def farm(max_orbs, cont):
    orbs_used = 0
    while True:
        start_quest = pyautogui.locateOnScreen("start_quest.png", confidence=0.8)
        retry = pyautogui.locateOnScreen("retry.png", confidence=0.8)
        tap_screen = pyautogui.locateOnScreen("tap_screen.png", confidence=0.8)
        close = pyautogui.locateOnScreen("close.png", confidence=0.8)
        purchase = pyautogui.locateOnScreen("purchase.png", confidence=0.8)
        result_screen = pyautogui.locateOnScreen("result_screen.png", confidence=0.8)
        continues = pyautogui.locateOnScreen("continue.png", confidence=0.8)
        buying = pyautogui.locateOnScreen("buying.png", confidence=0.8)
        if purchase != None and buying != None:
            if orbs_used + 5 > max_orbs:
                return "Finished"
            orbs_used += 5
            purchase = pyautogui.center(purchase)
            pyautogui.click(purchase)
        elif start_quest != None:
            start_quest = pyautogui.center(start_quest)
            pyautogui.click(start_quest)
        elif retry != None:
            retry = pyautogui.center(retry)
            pyautogui.click(retry)
        elif tap_screen != None:
            tap_screen = pyautogui.center(tap_screen)
            pyautogui.click(tap_screen)
        elif close != None:
            close = pyautogui.center(close)
            pyautogui.click(close)
        elif result_screen != None:
            result_screen = pyautogui.center(result_screen)
            pyautogui.click(result_screen)
        elif continues != None and cont == "y":
            continues = pyautogui.center(continues)
            pyautogui.click(continues)
        time.sleep(5)


quest = "this is placement text"
while quest == "this is placement text":
    print("Welcome to BBS Auto Farm!\nPress enter to continue")
    quest = input()

print("What is the maximum amount of orbs you would like to spend?")
max_orbs = int(input("Enter max number of orbs: "))
cont = input("Would you like to use revival candles? (y/n): ")
print("Starting BBS Auto Farm!")
print(farm(max_orbs, cont))
