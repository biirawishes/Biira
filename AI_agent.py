import asyncio
from telegram import Bot
from telegram.constants import ParseMode
import telegram.error

# Use environment variables or a secure vault for real deployment
BOT_TOKEN = "8105144524:AAG3Fguk29tG5VifIrXVSHrRI9yhFpN6ejo"
CHAT_ID = "-1002752208616"  # Can be a user ID, group ID, or @channelusername

async def post_to_telegram(text_content):
    """
    Sends a text message to a specified Telegram chat or channel.

    Args:
        text_content (str): The message to send.
    """
    if not text_content:
        print("Error: Text content cannot be empty.")
        return

    print("Attempting to post to Telegram...")

    try:
        # Create bot instance
        bot = Bot(token=BOT_TOKEN)

        # Send the message (must be awaited)
        await bot.send_message(
            chat_id=CHAT_ID,
            text=text_content,
            parse_mode=ParseMode.MARKDOWN
        )

        print("✅ Successfully posted to Telegram!")

    except telegram.error.TelegramError as e:
        print(f"❌ Telegram API error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    # Define your post content
    my_post = "Hello from Trish\n\nThis message was sent automatically at *9:00 PM*."
    
    # Run the async function
    asyncio.run(post_to_telegram(my_post))