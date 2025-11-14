import pyautogui
import time

print("Starting automation in 5 seconds...")
time.sleep(5)

click_sequence = [
    (33, 36),     # 1
    (614, 986),   # 2
    (604, 804),   # 3
    (153, 766),   # 4
    (364, 699),   # 5
    (110, 876),   # 6
    (111, 851),   # 7
    (411, 561),   # 8
    (224, 674),   # 9
    (826, 547),   # 10
    (609, 614),   # 11
    (1058, 553)   # 12
]

for i, (x, y) in enumerate(click_sequence):
    print(f"Clicking position {i+1}: ({x}, {y})")
    pyautogui.click(x, y)

    # Default pause
    if i < 7:
        time.sleep(0.7)
    else:
        time.sleep(1.2)

    # Scroll after 2nd click
    if i == 1:
        print("Pausing briefly before scrolling...")
        time.sleep(2)
        print("Moving mouse over scrollable area...")
        pyautogui.moveTo(600, 800)
        print("Scrolling slightly...")
        pyautogui.scroll(-235)
        time.sleep(0.75)

    # Paste after 4th click
    if i == 3:
        print("Extra pause before click 4 (input box)...")
        time.sleep(1.25)
        print("Repositioning mouse gently before click...")
        pyautogui.moveTo(x, y)
        time.sleep(0.75)
        pyautogui.click()
        print("Click 4 done. Waiting for input to activate...")
        time.sleep(1.25)
        print("Now pasting clipboard content (Ctrl+V)...")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1.25)

    # Slight slowdown after click 6 → 7
    if i == 5:
        print("Slowing down after click 6...")
        time.sleep(1.4)

    # Slight slowdown after click 7
    if i == 6:
        print("Slowing down after click 7...")
        time.sleep(1.8)

# Big scroll AFTER final click
print("Final click complete. Performing big scroll...")
pyautogui.moveTo(752, 482)
pyautogui.scroll(-7000)
time.sleep(0.5)