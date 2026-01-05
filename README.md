# Academic Workflow Automation Tool

Python automation script to streamline repetitive transcript access workflow in SLU's student information system. Reduces 9-12 manual clicks per transcript to a single automated sequence, preventing repetitive strain injury and freeing up cognitive bandwidth for actual advising work.

## Problem Statement

As an academic advisor at Saint Louis University, I access 20+ student transcripts daily. Each transcript requires:
- 9-12 manual clicks through the university's student information system
- Navigating multiple nested menus
- Copying/pasting student IDs
- Scrolling through paginated results

**Impact:** 200+ unnecessary clicks per day, increased risk of repetitive strain injury, and cognitive fatigue from repetitive tasks.

## Solution

Automated click sequence using PyAutoGUI to replicate the exact workflow, reducing the process from ~30 seconds of manual clicking to a single script execution.

### Features
- **9-step automated click sequence** with configurable delays
- **Clipboard integration** for automatic student ID pasting
- **Smart scrolling** at specific steps to navigate paginated interfaces
- **Safety failsafe** - move mouse to top-left corner to abort
- **Customizable coordinates** for different screen resolutions

## Technical Implementation
```python
# Core automation loop
for i, (x, y) in enumerate(CLICK_SEQUENCE):
    pyautogui.click(x=x, y=y)
    
    # Paste student ID at designated step
    if i in PASTE_STEPS:
        pyautogui.hotkey("ctrl", "v")
    
    # Scroll to navigate paginated results
    if i in SCROLL_AFTER:
        pyautogui.scroll(SCROLL_AFTER[i])
```

### Tech Stack
- **Python 3.x**
- **PyAutoGUI** - Cross-platform GUI automation
- **Pillow** - Screenshot functionality for failsafe

## Installation
```bash
# Clone repository
git clone https://github.com/hmierz/Academic-Workflow-Automation.git
cd Academic-Workflow-Automation

# Install dependencies
pip install pyautogui pillow

# Run script
python transcript_clicker.py
```

**Windows users:** Double-click `run_clicker.bat` for quick execution.

## Configuration

### Adjusting Click Coordinates

The script uses screen coordinates that may need adjustment for different displays:
```python
CLICK_SEQUENCE = [
    (796, 485),   # Step 1: Click student lookup
    (1005, 744),  # Step 2: Select transcript menu
    # ... add your coordinates
]
```

**To find coordinates:** Run this helper script:
```python
import pyautogui
import time
time.sleep(3)
print(pyautogui.position())  # Move mouse and check terminal
```

### Adjusting Timing

Some systems may need longer delays between steps:
```python
SLEEP_AFTER = {
    0: 0.5,   # 500ms after step 1
    4: 1.0,   # 1 second after paste step
}
```

## Usage Workflow

1. Copy student ID to clipboard
2. Navigate to starting screen in SLU system
3. Run script: `python transcript_clicker.py`
4. Script executes 9-step sequence automatically
5. Transcript opens ready for review

**Safety:** Mouse failsafe enabled - move cursor to top-left corner to abort at any time.

## Impact

**Time savings:**
- Manual process: ~30 seconds × 20 transcripts = 10 minutes/day
- Automated process: ~15 seconds × 20 transcripts = 5 minutes/day
- **Net savings: ~20 hours/year**

**Health benefits:**
- Reduced repetitive clicking by ~200 clicks/day
- Lower risk of carpal tunnel syndrome
- Reduced cognitive load from repetitive tasks

**Scalability:**
- Template adaptable to other university workflows
- Coordinates easily reconfigured for different systems
- Could be extended to batch processing multiple transcripts

## Limitations & Future Work

**Current limitations:**
- Coordinates are screen-resolution dependent
- Requires exact window positioning
- Single-system only (SLU's specific interface)

**Potential improvements:**
- [ ] Image recognition to auto-detect UI elements (less brittle than coordinates)
- [ ] Batch processing mode for multiple student IDs
- [ ] GUI interface for coordinate configuration
- [ ] Cross-platform coordinate adjustment
- [ ] Integration with student ID roster CSV for bulk operations
- [ ] Error handling for timeout/failed clicks

## Why This Matters

This project demonstrates:
- **Process improvement mindset** - identifying workflow bottlenecks
- **Quantitative impact analysis** - measuring time/health benefits
- **Practical automation skills** - Python, GUI automation, workflow optimization
- **Real-world application** - solving actual business problems, not just exercises

In operations analyst roles, identifying and automating repetitive processes is core work. This project shows that skillset in action.

## Disclaimer

This tool is designed for legitimate workflow automation within authorized systems. Users are responsible for ensuring compliance with their organization's automation policies.

## License

MIT License - see LICENSE file for details.

## Contact

Haley Mierz  
[GitHub](https://github.com/hmierz) • [LinkedIn](https://linkedin.com/in/haley-mierz)

Built to improve daily workflow efficiency at Saint Louis University.
