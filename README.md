# BBS-Auto-Farm

**Bleach Brave Souls MUST be in 1600x900 aspect ratio in order for the images to be located**

### Features
* Auto Farm any Quest
* Auto Farm any Co-op Quest
   * If you choose not to use candles for Co-op quest, if the quest is not completed within 10 minuets of your death a candle will be used in order to keep the cycle going

### Ensure you have the proper python packages:
To run this you must be able to run python files on your computer
```
pip install pyautogui
pip install opencv-python
pip install pysimplegui

```

### Once Everything is installed:
1. Find the quest you want to farm
2. Go to the prepare for quest page
3. Run auto.py
5. Follow command line GUI
6. Once it says "Starting BBS Auto Farm" navigate to Bleach Brave Souls and AFK

## New To Programming?
### Installation Guide for Windows (If already installed skip to step 7)
1. If you dont have [Git for Windows](https://gitforwindows.org/){:target="_blank"} installed download it from here
2. Once Git for Windows is installed, launch the `Git CMD` app
3. Once in the terminal, paste these commands
   ```
   mkdir github
   cd github
   git clone https://github.com/ZainMI/BBS-Auto-Farm.git
   cd BBS-Auto-Farm
   
   ```
4. Paste this into terminal
   ```
   python --version
   
   ```
   1. If you get this output
      
      `Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.`
      
      Type `python` then press enter to bring you to the Microsoft store and install Python
5. Once Python is installed paste these into the terminal
   ```
   pip install pyautogui
   pip install opencv-python
   pip install pysimplegui
   
   ```
6. To run paste this into terminal
   ```
   python auto.py
   
   ```
7. If BBS Auto Farm is already installed paste these into terminal
   1. Open `Git CMD`
   2. Paste these into the terminal
      ```
      cd github/BBS-Auto-Farm
      python auto.py
      
      ```

### Installation Guide for Linux (If already installed skip to step 5)
1. Open Terminal
2. Paste these into terminal
   1. If you don't have `git` installed paste this then type your password and press `y` when prompted
      ```
      sudo apt install git
      
      ```
   2. Once git is installed
      ```
      mkdir github
      cd github
      git clone https://github.com/ZainMI/BBS-Auto-Farm.git
      cd BBS-Auto-Farm
      
      ```
3. Paste these into terminal
   1. If you don't have `pip` installed paste this then type your password and press `y` when prompted
      ```
      sudo apt install python3-pip
      
      ```
   2. Once pip is installed
      ```
      pip install pyautogui
      pip install opencv-python
      pip install pysimplegui
      
      ```
4. To run paste this into terminal
   ```
   python3 auto.py
   
   ```
5. If BBS Auto Farm is already installed paste these into terminal
   ```
   cd github/BBS-Auto-Farm
   python3 auto.py
   
   ```
