import openpyxl
from PIL import Image
import pytesseract
import pyautogui
import time

# Prendre une capture d'écran
screenshot = pyautogui.screenshot("screenshot.png")
print("Capture d'écran enregistrée.")

screenshot = Image.open("screenshots\Screenshot1.png")

text = pytesseract.image_to_string(screenshot)

#print(text)
print("Fin du défilement automatique.")