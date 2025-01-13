from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKENTELEGRAM")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text('Hola! No se que estoy haciendo :D')
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Usa /start para comenzar o /help para obtener ayuda.')
async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    filename = 'Prueba_Telegram.txt'

    try:
        with open(filename, 'r') as file:
            content = file.read()
        await update.message.reply_text(content)
    except FileNotFoundError:
        await update.message.reply_text(f"No se encontró el archivo: {filename}")
    except Exception as e:
        # Si ocurre un error inesperado
        await update.message.reply_text(f"Hubo un error al leer el archivo: {e}")
        
def main():
    app = Application.builder() .token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("show", show))
    print("El bot funciona")
    app.run_polling()
if __name__ == "__main__":
    main()
