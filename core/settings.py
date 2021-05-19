"""
Bot settings manager
"""

from filebot.models import Settings
from typing import Optional


def get_settings() -> Optional[Settings]:
    """
    Get bot settings
    """
    return Settings.objects.first()


def set_settings(share_text: str, contacts_text: str, start_message_text: str):
    """
    Edit bot settings
    """
    bot_settings = get_settings()
    if bot_settings is None:
        bot_settings = Settings()
    bot_settings.start_message_text = start_message_text
    bot_settings.contacts_text = contacts_text
    bot_settings.share_text = share_text
    bot_settings.save()
