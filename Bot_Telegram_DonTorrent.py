from telethon import TelegramClient
import asyncio

ENDPOINTS = ['/descargar-peliculas','/peliculas/4K', '/descargar-peliculas/hd', '/descargar-series', '/series/hd', '/documentales']

api_id = '28004723'
api_hash = 'edd51b041abd5c11bd537cfe6cb6ee94'
channel_username = 'DonTorrent'

sesion_name = 'mi_sesion'
client = TelegramClient(sesion_name, api_id, api_hash)

async def main():
    try:
        print(f"Conectando al canal: {channel_username}")
        
        async for message in client.iter_messages(channel_username):
            if message.text:
                if 'Dominio Oficial' in message.text:
                    if '✅' in message.text:
                        #print(f"Nuevo Dominio disponible: {message.text}")
                        parts = message.text.split(') ')
                        if len(parts) > 1:
                            url_part = parts[1].split(' (')[0]
                        print(f"Encontrada: {url_part}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
