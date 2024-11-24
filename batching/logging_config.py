import os
import logging
from datetime import datetime

# Creates logs/ directory if not existing
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Logging configuration
LOG_FILE = os.path.join(
    LOG_DIR, f"batches_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log"
)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Console logging perhaps unnecessary
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
logging.getLogger().addHandler(console_handler)

logger = logging.getLogger()
