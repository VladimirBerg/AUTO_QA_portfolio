from loguru import logger
import sys
from pathlib import Path

def setup_logger(test_name: str = "test"):
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logger.remove()
    logger.add(
        log_dir / f"{test_name}.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="DEBUG",
        rotation="1 MB"
    )
    logger.add(sys.stdout, format="{time:HH:mm:ss} | {level} | {message}", level="INFO")
    return logger
