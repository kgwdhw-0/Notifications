import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

def send_sms(to_number: str, message: str):
    """
    Uses Textbelt’s free tier to send one SMS per day.
    """
    payload = {
        'phone': to_number,
        'message': message,
        'key': settings.TEXTBELT_KEY,
    }
    resp = requests.post('https://textbelt.com/text', data=payload)
    result = resp.json()

    if not result.get('success'):
        # Log the reason—e.g. quota reached, invalid number, etc.
        logger.error(f"Textbelt error: {result.get('error')}")
        raise RuntimeError(f"SMS send failed: {result.get('error')}")
    logger.info(f"[Textbelt SMS] sent to {to_number}")