import logging
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = PROJECT_ROOT / "logs"

RUN_TIMESTAMP = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

def get_logger(name):
    logger = logging.getLogger(name)

    if not logger.handlers:
        LOG_DIR.mkdir(exist_ok=True)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        log_file = LOG_DIR / f"test_run_{RUN_TIMESTAMP}.log"

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)

    return logger
