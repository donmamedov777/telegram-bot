from telethon import TelegramClient, events

api_id = 24246327
api_hash = '69a698c38c58273a05d2837a93415b7f'
session_name = 'my_session'

keywords = ['фитпасс', 'fitpass', 'фитпас']

target_chats = [
    'https://t.me/mybatumi_chat',
    'https://t.me/tbilisi_chatg',
    'https://t.me/mytbilisi_chat'
]

notify_group = '@notificationsqa'

# Вставляем твой токен сюда
bot_token = '7818798124:AAH5XJ8Ws_oCciNLZKuvzqr5ZOueDZcUq0g'

client = TelegramClient(session_name, api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=target_chats))
async def handler(event):
    msg = event.raw_text.lower()
    if any(word in msg for word in keywords):
        chat = await event.get_chat()
        chat_name = getattr(chat, 'title', 'Неизвестный чат')
        await client.send_message(
            notify_group,
            f'🔔 Найдено ключевое слово в чате: {chat_name}

💬 Сообщение:
{event.raw_text}'
        )

client.start()
print("✅ Бот запущен. Слушаю чаты...")
client.run_until_disconnected()
