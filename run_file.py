import pyautogui 
import time
import os
from record import *


folder_path = "auto_sample_create/vital_files" #change path
folder_path_rel = 'vital_files' #zip file name without zip #fixed
audio_save_folder = 'sample_audio'


def play_note(note_key, note_time):
    with pyautogui.hold(note_key):
        time.sleep(note_time)

def open_vital():
    pyautogui.hotkey('alt', 'f2')  # 'super' key often corresponds to the Windows key or Command key
    time.sleep(2)
    pyautogui.write('Vital')  # Replace with the application you want to open
    # Press Enter to launch the application
    pyautogui.press('enter')
    # Wait for the program to open
    time.sleep(2)

def preset_move(that_file_path):
    file_menu_x, file_menu_y = 901, 94
    open_menu_x, open_menu_y = 901, 154
    ## open preset file
    pyautogui.moveTo(file_menu_x, file_menu_y, duration=0.1)
    pyautogui.click()

    pyautogui.moveTo(open_menu_x, open_menu_y, duration=0.1)
    pyautogui.click()

    pyautogui.moveTo(1777, 50, duration=0.1)
    pyautogui.click()

    that_file_path_list = that_file_path.split("/")
 

    for i in that_file_path_list:
        pyautogui.write(i)
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
    
def open_preset_play(that_folder_path):
    preset_list = os.listdir(that_folder_path)

    for i in range(len(preset_list)):
        time.sleep(0.5)
        pyautogui.write(preset_list[i])
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.3)    
    
        # play notes
        curr_vital_name = preset_list[i].split(".")[0]

        record_process = start_recording(audio_save_folder + "/" + curr_vital_name + ".wav") #start recording

        note_list = ['a','s','d', 'f', 'g', 'h', 'j', 'k']
        for j in note_list:
            play_note(j, 0.15)

        stop_recording(record_process)
        
        if i != len(preset_list)-1:
            file_menu_x, file_menu_y = 901, 94
            open_menu_x, open_menu_y = 901, 154
            ## open preset file
            pyautogui.moveTo(file_menu_x, file_menu_y, duration=0.1)
            pyautogui.click()

            pyautogui.moveTo(open_menu_x, open_menu_y, duration=0.1)
            pyautogui.click()
        





def close_vital():
    close_vital_x, close_vital_y = 1189, 56
    pyautogui.moveTo(close_vital_x, close_vital_y, duration=0.1)
    pyautogui.click()


if __name__ == '__main__':
    vital_zip = os.listdir(folder_path_rel)[0]

    if not os.path.exists(audio_save_folder):
        os.makedirs(audio_save_folder)

  

    os.system('unzip -j ' + folder_path_rel + "/" + vital_zip + " -d " + folder_path_rel)
    os.system('rm ' + folder_path_rel + "/" + vital_zip)
    open_vital()
    preset_move(folder_path)
    open_preset_play(folder_path_rel)
    close_vital()
    os.system("rm -r " + folder_path_rel + "/*")
    os.system("zip -r sample_audio.zip sample_audio/")
    os.system("rm -rf sample_audio/*")


    # print(pyautogui.position())
