from telethon import TelegramClient
import requests
from bs4 import BeautifulSoup
import asyncio
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os
import json
TOKEN = os.environ.get("TOKENTELEGRAM")

#CHAT_ID = < REPLACE WITH YOUR CHAT ID >
CHAT_ID = ""

bot = Bot(token=TOKEN)

ENDPOINTS = ['/descargar-peliculas', '/peliculas/4K', '/descargar-peliculas/hd', '/descargar-series', '/series/hd', '/documentales']

CATEGORIAS = {
    '/descargar-peliculas': 'Peliculas SD 🎥',
    '/peliculas/4K': 'Peliculas 4K 🌟',
    '/descargar-peliculas/hd': 'Peliculas HD 📺',
    '/descargar-series': 'Series SD 📺',
    '/series/hd': 'Series HD 📡',
    '/documentales': 'Documentales 🎬'
}
BASE_URL = 'https://dontorrent.auction'

API_ID = os.environ.get("TELEGRAM_API_ID")
API_HASH = os.environ.get("TELEGRAM_API_HASH")
channel_username = 'DonTorrent'

sesion_name = 'mi_sesion'
client = TelegramClient(sesion_name, API_ID, API_HASH)

def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

session=get_tor_session()

async def main():
    results = []
    try:
        print(f"Conectando al canal: {channel_username}")

        async for message in client.iter_messages(channel_username):
            if message.text:
                if 'Dominio Oficial' in message.text and '✅' in message.text:
                    parts = message.text.split(') ')
                    if len(parts) > 1:
                        url_part = parts[1].split(' (')[0]
                       # print(f"Encontrada: {url_part}")

                        for endpoint in ENDPOINTS:
                            message = ''
                            message += "================================================\n"
                            message += '                      ' + CATEGORIAS[endpoint] +'\n'
                            message += "================================================\n"
                            print("==============================================================")
                            print('                      ' + CATEGORIAS[endpoint])
                            print("==============================================================")
                            full_url = f"{url_part}{endpoint}"
                            try:
                                response = session.get(full_url, timeout=100)
                                if response.status_code == 200:
                                    #print(f"HTML obtenido de {full_url}:\n{response.text[:500]}...")

                                    soup = BeautifulSoup(response.text, 'html.parser')
                                    noticias_div = soup.find('div', class_='noticias')


                                    text_center = noticias_div.find_all('div', class_='text-center')
                                    if text_center:
                                        #for div in text_center:
                                        links = text_center[0].find_all('a', href=True)
                                        if links:
                                            for link in links:
                                                link_url = link['href'].split('/')[-1].replace('-', ' ')
                                                print(link_url)
                                                message+=link_url + '\n'

                                    else:
                                        print("No se encontró 'noticias' en el HTML.")
                                else:
                                    print(f"Error al acceder a {full_url}: {response.status_code}")
                            except requests.RequestException as e:
                                print(f"Error en la petición a {full_url}: {e}")

                            with open("./usuarios_registrados.json", 'r') as f:
                                ids= json.load(f)

                            for id in ids:
                                await bot.send_message(chat_id =id, text=message)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
