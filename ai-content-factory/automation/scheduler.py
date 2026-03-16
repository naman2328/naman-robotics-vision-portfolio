"""Simple scheduler utility.

Use OS-native schedulers for production:
- Windows Task Scheduler
- cron (Linux/macOS)
"""

import subprocess
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]


def run_daily(hour: int = 9, minute: int = 0) -> None:
    while True:
        now = time.localtime()
        if now.tm_hour == hour and now.tm_min == minute:
            subprocess.run(["python", "automation/pipeline.py"], cwd=BASE_DIR, check=False)
            time.sleep(60)
        time.sleep(1)


if __name__ == "__main__":
    run_daily()
