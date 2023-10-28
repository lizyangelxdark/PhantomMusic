from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://userbot:userbot@cluster0.yyijp36.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/618310dd8b8cf0fc5270d.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2030bea6c41b37ec65a8d.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/RoxyTeams")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RoxyBots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
