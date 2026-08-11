from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"


def save_screenshot(driver, test_name):
    SCREENSHOT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    screenshot_path = (
            SCREENSHOT_DIR
            / f"{test_name}_{timestamp}.png"
    )

    driver.save_screenshot(str(screenshot_path))

    return screenshot_path
