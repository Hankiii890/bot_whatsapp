# services/db.py
from types import SimpleNamespace

_users = {}  # chat_id → SimpleNamespace(chat_id, lang, state)

def get_or_create_user(chat_id: str) -> SimpleNamespace:
    if chat_id not in _users:
        _users[chat_id] = SimpleNamespace(chat_id=chat_id, lang='en', state='idle')
    return _users[chat_id]

def update_user_state(chat_id: str, state: str = None, lang: str = None) -> None:
    user = _users.get(chat_id)
    if not user:
        return
    if state is not None:
        user.state = state
    if lang is not None:
        user.lang = lang
