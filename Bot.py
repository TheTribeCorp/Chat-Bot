```python
# bot.py

import os
from io import BytesIO
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image, ImageDraw, ImageFont

# Initialize the Telegram Bot
updater = Updater(token=os.environ.get("TELEGRAM_API_TOKEN"), use_context=True)
dispatcher = updater.dispatcher

# Define a command handler for the text-to-image conversion
def text_to_image(update, context):
    text = update.message.text
    image = create_image(text)
    bio = BytesIO()
    bio.name = 'image.png'
    image.save(bio, 'PNG')
    bio.seek(0)
    update.message.reply_photo(bio)

# Helper function to create an image from text
def create_image(text):
    font = ImageFont.truetype("arial.ttf", 25)
    image = Image.new('RGB', (400, 100), color = (73, 109, 137))
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, fill=(255,255,0), font=font)
    return image

# Define a message handler for processing all messages
def echo(update, context):
    update.message.reply_text("I only understand the /texttoimage command.")

# Create handlers and add them to the dispatcher
text_to_image_handler = CommandHandler('texttoimage', text_to_image)
dispatcher.add_handler(text_to_image_handler)
echo_handler = MessageHandler(Filters.text & ~Filters.command, echo)
dispatcher.add_handler(echo_handler)

# Start the Bot
updater.start_polling()
updater.idle()
```
