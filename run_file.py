import pyautogui 
import time
import os

program = "C:\Program Files\Vital\Vital.exe"
file_path = "C:\\Users\\SKT\\Desktop\\run_auto\\Pluck_CTGAN_synthesizer\\Pluck_CTGAN_synthesizer\\AIU_Preset_4.vital"



def play_note(note_key):
    with pyautogui.hold(note_key):
        time.sleep(0.15)

def open_vital():
    pyautogui.hotkey('win', 'r')  # Opens the Run dialog
    time.sleep(1)
    pyautogui.write(program)  # Type the program name
    pyautogui.press('enter')  # Press Enter to open the program

    # Wait for the program to open
    time.sleep(2)

def preset_and_play(that_file_path):
    file_menu_x, file_menu_y = 1313, 62
    open_menu_x, open_menu_y = 1313, 142
    ## open preset file
    pyautogui.moveTo(file_menu_x, file_menu_y, duration=0.1)
    pyautogui.click()

    pyautogui.moveTo(open_menu_x, open_menu_y, duration=0.1)
    pyautogui.click()

    pyautogui.write(that_file_path)  # Type the full file path
    pyautogui.press('enter')  # Press Enter to open the file


    #play notes
    note_list = ['a','s','d', 'f', 'g', 'h', 'j', 'k']

    for i in note_list:
        play_note(i)

def close_vital():
    close_vital_x, close_vital_y = 1760, 28
    pyautogui.moveTo(close_vital_x, close_vital_y, duration=0.1)
    pyautogui.click()


if __name__ == '__main__':
    open_vital()
    preset_and_play("C" + file_path)
    close_vital()
