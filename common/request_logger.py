from flask import request, g
import time
import datetime
import logging
import json_log_formatter


formatter = json_log_formatter.JSONFormatter()
json_handler = logging.FileHandler(filename='app_log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('json_logger')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


def start_timer():
    """It has to record time before each request"""
    g.start = time.time()


def log_request(response):
    """Calculates duration and save it in a log file"""
    now = time.time()
    duration = round((now * 1000) - (g.start * 1000))
    dt = datetime.datetime.fromtimestamp(now)

    log_params = {
        'method': request.method,
        'path': request.path,
        'status': response.status_code,
        'duration': f"{duration}ms",
        'time': dt
    }

    logger.info('Request', extra=log_params)
    return response
