import logging
import logging.config
import ntplib
from time import ctime
from typing import AsyncGenerator, Optional, Union  # Add this import

from pyrogram import Client, __version__, types
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import API_HASH, API_ID, BOT_TOKEN, LOG_STR, SESSION, USER_SESSION
from utils import temp, scheduler

# Synchronize time
def synchronize_time():
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request('pool.ntp.org')
        current_time = response.tx_time
        import os
        os.system(f'date {ctime(current_time)}')
        print("Time synchronized successfully!")
    except Exception as e:
        print("Failed to synchronize time:", e)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Pyrogram client
User = Client("userBot", API_ID, API_HASH, session_string=USER_SESSION)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        synchronize_time()  # Synchronize time before starting
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await User.start()
        self._____ = User.invoke
        self.____________________ = User.resolve_peer
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        scheduler.start()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = "@" + me.username
        logging.info(
            f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}."
        )
        logging.info(LOG_STR)

    async def stop(self, *args):
        await User.stop()
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially."""
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(
                chat_id, list(range(current, current + new_diff + 1))
            )
            for message in messages:
                yield message
                current += 1

app = Bot()

if __name__ == "__main__":
    app.run()
