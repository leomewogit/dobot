from os import environ

from telebot.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from _bot import bot

bot_name = environ.get('bot_name', 'Assistant DigitalOcean')


def start(d: Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(
            text='Add Account',
            callback_data='add_account'
        ),
        InlineKeyboardButton(
            text='List accounts',
            callback_data='manage_accounts'
        ),
        InlineKeyboardButton(
            text='Create droplets',
            callback_data='create_droplet'
        ),
        InlineKeyboardButton(
            text='Check droplets',
            callback_data='manage_droplets'
        ),
    )
    t = f'Welcome <b>{bot_name}</b>\n\n' \
        'You can manage DigitalOcean accounts, create VPS, etc.\n\n' \
        'Quick Command:\n' \
        '/start - Start Bot\n' \
        '/add_do - Add account\n' \
        '/sett_do - list accounts\n' \
        '/bath_do - batch test accounts\n' \
        '/add_vps - Make droplets\n' \
        '/sett_vps - list droplets\n' \
        ' \n'
    bot.send_message(
        text=t,
        chat_id=d.from_user.id,
        parse_mode='HTML',
        reply_markup=markup
    )
