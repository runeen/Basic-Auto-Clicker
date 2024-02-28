import keyboard
import pyautogui

hotkey = "c"

def wait_until_key_released():
	while True:
		if not keyboard.is_pressed(hotkey):
			break
		

def spam():
	while True:
		if keyboard.is_pressed(hotkey):
			wait_until_key_released()
			break
		pyautogui.click()

while True:
	if keyboard.is_pressed(hotkey):
			wait_until_key_released()
			spam()