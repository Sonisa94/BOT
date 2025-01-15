from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging
import os
import json

#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#logger = logging.getLogger(__name__)

USUARIOS_REGISTRADOS_FILE = "usuarios_registrados.json"
TOKEN = os.environ.get("TOKENTELEGRAM")

def cargar_usuarios_registrados():
    if os.path.exists(USUARIOS_REGISTRADOS_FILE):
        with open(USUARIOS_REGISTRADOS_FILE, 'r') as f:
            return json.load(f)
    return []

def guardar_usuarios_registrados(usuarios):
    with open(USUARIOS_REGISTRADOS_FILE, 'w') as f:
        json.dump(usuarios, f)

async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    await update.message.reply_text(f"Hola {user.first_name}! Gracias por usarnos :D")
    usuarios_registrados = cargar_usuarios_registrados()
    if user.id not in usuarios_registrados:
        usuarios_registrados.append(user.id)
        guardar_usuarios_registrados(usuarios_registrados)
        print(f"Usuario registrado: {user.first_name} , ID: {user.id}")
    else:
        print(f"Usuario {user.first_name} ya está registrado.")

def main() -> None:
     app = Application.builder().token(TOKEN).build()
     app.add_handler(CommandHandler("start", start))

     app.run_polling()

if __name__ == '__main__':
    main()
