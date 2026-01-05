"""
Academic Workflow Automation Tool
Automates repetitive click sequence for accessing student transcripts in SLU's system.

Safety: Press Ctrl+C or move mouse to top-left corner to abort.
"""

import time
import sys

try:
    import pyautogui
except ImportError:
    print("Missing dependencies. Install with: pip install pyautogui pillow")
    sys.exit(1)

# Enable failsafe - move mouse to top-left corner to abort
pyautogui.FAILSAFE = True

# Click coordinates for transcript workflow
# NOTE: These coordinates are for 1920x1080 resolution and may need adjustment
CLICK_SEQUENCE = [
    (796, 485),   # Step 1: Student lookup button
    (1005, 744),  # Step 2: Transcript menu
    (854, 745),   # Step 3: Academic records
    (875, 743),   # Step 4: Select search field
    (877, 738),   # Step 5: Click to paste student ID
    (1194, 73),   # Step 6: Submit button
    (108, 194),   # Step 7: Select transcript
    (1194, 73),   # Step 8: Open transcript
    (1276, 193),  # Step 9: Final view
]

# Delay after each step (in seconds)
SLEEP_AFTER = {
    0: 0.5,  # After step 1
    1: 0.5,  # After step 2
    2: 0.5,  # After step 3
    3: 0.7,  # After step 4
    4: 1.0,  # After paste (longer to ensure paste completes)
    5: 0.7,  # After step 6
    6: 0.7,  # After step 7
    7: 0.7,  # After step 8
    8: 0.7,  # After step 9
}

# Steps where we paste student ID from clipboard (zero-indexed)
PASTE_STEPS = {4}

# Steps requiring scroll (negative = scroll down)
SCROLL_AFTER = {
    1: -300,   # Scroll down after step 2
    8: -800,   # Scroll down after step 9
}


def main():
    """Execute the automated click sequence."""
    print("=" * 60)
    print("Academic Workflow Automation Tool")
    print("=" * 60)
    print("\nStarting in 3 seconds...")
    print("SAFETY: Move mouse to top-left corner to abort at any time.\n")
    
    time.sleep(3)
    
    total_steps = len(CLICK_SEQUENCE)
    
    for i, (x, y) in enumerate(CLICK_SEQUENCE):
        step_num = i + 1
        print(f"[Step {step_num}/{total_steps}] Clicking at ({x}, {y})")
        
        # Execute click
        pyautogui.click(x=x, y=y)
        
        # Paste student ID if this is a paste step
        if i in PASTE_STEPS:
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "v")
            print(f"  → Pasted student ID")
        
        # Scroll if needed
        if i in SCROLL_AFTER:
            scroll_amount = SCROLL_AFTER[i]
            time.sleep(0.2)
            pyautogui.scroll(scroll_amount)
            print(f"  → Scrolled {abs(scroll_amount)} pixels {'down' if scroll_amount < 0 else 'up'}")
        
        # Wait before next step
        time.sleep(SLEEP_AFTER.get(i, 0.5))
    
    print("\n" + "=" * 60)
    print("Automation complete! Transcript should now be open.")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAborted by user (Ctrl+C)")
        sys.exit(0)
    except pyautogui.FailSafeException:
        print("\n\nFailsafe triggered (mouse moved to corner)")
        sys.exit(0)
