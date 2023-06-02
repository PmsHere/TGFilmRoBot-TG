import re
from os import environ

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get("SESSION", "Media_search")
API_ID = environ.get('API_ID', '4534665')
API_HASH = environ.get('API_HASH', '366f7a24d64c5d6578df57e3b5b03fa0')
BOT_TOKEN = environ.get('BOT_TOKEN', '5353888647:AAGdFBWN6rtdVuT-YhdO3xOiT0Z7gRagk8c')
USER_SESSION = environ.get('USER_SESSION', 'BQAckvgAAVchjwnPfDAxYJv30Kf5qiCzxF7Or1j0a6JpKP51MQtsVZ_VJA91MpVI61E6Settd9SBE4h5XePm6VDV3AZGrsJt0AMetzchBwRCPOFeb3jUVqsxyEnB6QJFnXbm22TxWYhWj244FUZvVs51S290mMgy6b7Bm_rteAodDh5vWd21zpKpG7PH5WbaKQn8VEzy6bc_UY31Wg1E-vdxZHx_l_VXzH7LxYXeRhwFWNhHq9ccFLOQ1Zhi55JROlpIvWKOvdQbHI2TaH_tu5j-EfdmcSZLTJmCvX5IRZxaZfkbfg8mhBnH2j9Tg6SRg7OuuCgN8VRuTXkYVSWykQjAwgVSAAAAAABctJvFAA')
# Bot settings
CACHE_TIME = int(environ.get("CACHE_TIME", 300))
USE_CAPTION_FILTER = bool(environ.get("USE_CAPTION_FILTER", False))
PICS = (
    environ.get(
        "PICS",
        "https://graph.org/file/332ccd03b44770a305559.jpg",
    )
).split()

# Admins, Channels & Users
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get('ADMINS', '1893684647').split()
]
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get('CHANNELS', '-1001682880445').split()
]
auth_users = [
    int(user) if id_pattern.search(user) else user
    for user in environ.get('AUTH_USERS', '').split()
]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001736005739')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = (
    int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
)
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://apollo:pmshere@cluster0.0gkxnrn.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "Telegram_files")

# Others 
DELETE_TIME = int(environ.get('DELETE_TIME', '300'))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1001390229228'))
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "MalluTorentzTG")
P_TTI_SHOW_OFF = is_enabled((environ.get("P_TTI_SHOW_OFF", "True")), True)
IMDB = is_enabled((environ.get("IMDB", "False")), False)
SINGLE_BUTTON = is_enabled((environ.get("SINGLE_BUTTON", "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '<pre>{file_name}</pre>\n\n<b>🔗𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞☞\n\nhttps://t.me/+WdzjOMj3tVY0YjJk\nhttps://t.me/+WdzjOMj3tVY0YjJk\nhttps://t.me/+WdzjOMj3tVY0YjJk</b>')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get(
    "IMDB_TEMPLATE",
    "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10",
)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get("INDEX_REQ_CHANNEL", LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get("FILE_STORE_CHANNEL", "-1001658035444")).split()]
MELCOW_NEW_USERS = is_enabled((environ.get("MELCOW_NEW_USERS", "True")), True)
PROTECT_CONTENT = is_enabled((environ.get("PROTECT_CONTENT", "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get("PUBLIC_FILE_STORE", "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += (
    "IMDB Results are enabled, Bot will be showing imdb details for you queries.\n"
    if IMDB
    else "IMBD Results are disabled.\n"
)
LOG_STR += (
    "P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n"
    if P_TTI_SHOW_OFF
    else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n"
)
LOG_STR += (
    "SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n"
    if SINGLE_BUTTON
    else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n"
)
LOG_STR += (
    f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n"
    if CUSTOM_FILE_CAPTION
    else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n"
)
LOG_STR += (
    "Long IMDB storyline enabled."
    if LONG_IMDB_DESCRIPTION
    else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n"
)
LOG_STR += (
    "Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n"
    if SPELL_CHECK_REPLY
    else "SPELL_CHECK_REPLY Mode disabled\n"
)
LOG_STR += (
    f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n"
    if MAX_LIST_ELM
    else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n"
)
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
