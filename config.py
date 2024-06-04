import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID",23226549))
API_HASH = getenv("API_HASH","2e6a1e4d566dad0f3e1d6ba9dadd32a3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://alisamusicc:alisamusicc@cluster0.1g7uzob.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500000000000))

OWNER_USERNAME = getenv("OWNER_USERNAME","toluzane")
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002015609420))

PUBLICELOGS = int(getenv("PUBLICELOGS", -1002015609420)) # Chat id of a group for Bot Added Messege/Leaved Messege U can Add Your Support Group id Aslo
GBANLOGS = int(getenv("GBANLOGS", -1002015609420))
# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6663326472))
OWNER = int(getenv("OWNER",6663326472))
## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/korsanfed")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/VIP_sohbet_Arkadaslik")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

AMBOT = [
    "💞",
    "🔎",
    "🔍",
    "🧪",
    "💣",
     "⚡️",
     "🔥",
     "🕺",
     "🎩",
     "🌈",
     "🍷",
     "🥂",
     "🍾",
    "🥃",
    "🥤",
    "🍽",
    "🍭",
    "🚗",
    "🚕",
    "🚓",
    "🚑",
    "🚀",
    "💎",
    "🔮",
    "🪄",
    "💌",
    "⁉️",
    "💤",
    "🧨"
]


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "3324f06d5deb44b1b677d3a525ebd3d9")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "cafbda1eaa8b44e2bcdf8af91d3eb85f")

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "900"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "900"))

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "string-session-gir")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/306d1e2e683b4dc0b56f8.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )