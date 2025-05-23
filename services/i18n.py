# services/i18n.py
_translations = {
    'start_text': {
        'en': 'Welcome! Use /to <lang> to select your target language.',
        'ru': 'Привет! Используй /to <lang>, чтобы выбрать язык перевода.',
        'zh': '欢迎！使用 /to <lang> 来选择目标语言。'
    },
    'pair_saved': {
        'en': '✅ Language set successfully.',
        'ru': '✅ Язык успешно сохранён.',
        'zh': '✅ 语言设置成功。'
    }
}

def t(lang: str, key: str) -> str:
    return _translations.get(key, {}).get(lang) or _translations.get(key, {}).get('en', '')
