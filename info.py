# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '22349465'))
API_HASH = environ.get('API_HASH', '3732e079c4125690226d8e7b4e028ca4')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 10))
PICS = (environ.get('PICS', 'https://graph.org/file/511d44d1131b2a889a176.jpg https://graph.org/file/a963b6c7791ef421be902.jpg https://graph.org/file/48118f8f5dec27fa9c15f.jpg https://graph.org/file/510e374a065a9e3a9b74a.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/b69af2db776e4e85d21ec.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/How_To_Open_Linkl")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001786924542'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5469498838').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# auth_channel means force subscribe channel.
# if REQUEST_TO_JOIN_MODE is true then force subscribe work like request to join fsub, else if false then work like normal fsub.
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False)) # Set True Or False
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False)) # Set True Or False (This try again button is only for request to join fsub not for normal fsub)
auth_channel = environ.get('AUTH_CHANNEL', '') # give your force subscribe channel id here else leave it blank
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002115486459')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002059362019')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002197083917')).split()]
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "tjbot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'tjbotdatabase')

# Premium And Referal Settings
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# If PREMIUM_AND_REFERAL_MODE is True Then Fill Below Variable, If Flase Then No Need To Fill.
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/24656c495f877f71e58f4.jpg')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- á´€á´ á´€ÉªÊŸá´€Ê™ÊŸá´‡ á´˜ÊŸá´€É´s - \n\n- 10Ê€s - 1 á´¡á´‡á´‡á´‹\n- 30Ê€s - 1 á´á´É´á´›Êœs\n- 100Ê€s - 3 á´á´É´á´›Êœs\n- 180Ê€s - 6 á´á´É´á´›Êœs\n- 350Ê€s - 12 á´á´É´á´›Êœs\nðŸŽ á´˜Ê€á´‡á´Éªá´œá´ Ò“á´‡á´€á´›á´œÊ€á´‡s ðŸŽ\n\nâ—‹ É´á´ É´á´‡á´‡á´… á´›á´ á´ á´‡Ê€ÉªÒ“Ê\nâ—‹ É´á´ É´á´‡á´‡á´… á´›á´ á´á´˜á´‡É´ ÊŸÉªÉ´á´‹\nâ—‹ á´…ÉªÊ€á´‡á´„á´› Ò“ÉªÊŸá´‡s\nâ—‹ á´€á´…-Ò“Ê€á´‡á´‡ á´‡xá´˜á´‡Ê€Éªá´‡É´á´„á´‡\nâ—‹ ÊœÉªÉ¢Êœ-sá´˜á´‡á´‡á´… á´…á´á´¡É´ÊŸá´á´€á´… ÊŸÉªÉ´á´‹\nâ—‹ á´á´œÊŸá´›Éª-á´˜ÊŸá´€Êá´‡Ê€ sá´›Ê€á´‡á´€á´ÉªÉ´É¢ ÊŸÉªÉ´á´‹s\nâ—‹ á´œÉ´ÊŸÉªá´Éªá´›á´‡á´… á´á´á´ Éªá´‡s & sá´‡Ê€Éªá´‡s\nâ—‹ êœ°á´œÊŸÊŸ á´€á´…á´ÉªÉ´ sá´œá´˜á´˜á´Ê€á´›\nâ—‹ Ê€á´‡Ç«á´œá´‡sá´› á´¡ÉªÊŸÊŸ Ê™á´‡ á´„á´á´á´˜ÊŸá´‡á´›á´‡á´… ÉªÉ´ 1Êœ Éªêœ° á´€á´ á´€ÉªÊŸá´€Ê™ÊŸá´‡\n\nâœ¨ á´œá´˜Éª Éªá´… - <code>abhishek.ly@axl</code>\n\ná´„ÊŸÉªá´„á´‹ á´›á´ á´„Êœá´‡á´„á´‹ Êá´á´œÊ€ á´€á´„á´›Éªá´ á´‡ á´˜ÊŸá´€É´ /myplan\n\nðŸ’¢ á´á´œsá´› sá´‡É´á´… sá´„Ê€á´‡á´‡É´sÊœá´á´› á´€Ò“á´›á´‡Ê€ á´˜á´€Êá´á´‡É´á´›\n\nâ€¼ï¸ á´€Ò“á´›á´‡Ê€ sá´‡É´á´…ÉªÉ´É¢ á´€ sá´„Ê€á´‡á´‡É´sÊœá´á´› á´˜ÊŸá´‡á´€sá´‡ É¢Éªá´ á´‡ á´œs sá´á´á´‡ á´›Éªá´á´‡ á´›á´ á´€á´…á´… Êá´á´œ ÉªÉ´ á´›Êœá´‡ á´˜Ê€á´‡á´Éªá´œá´</b>')
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'iam_abhi_boy') # owner username without @

# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Movie_ Studio_Request')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Mo viestudioabhi')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/tj_bots_z')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Movije_studio_support_group') # Support Chat Link Without https:// or @

# True Or False
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Token Verification Info :
VERIFY = bool(environ.get('VERIFY', False))
VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', False))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
# if verify second shortner is True then fill below url and api
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://t.me/tj_bots_zyz/3')

# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', True))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shortxlinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '40953a3cd91c66b8fb8ebc21e301dd3d87e29607')

# Others
MAX_B_TN = environ.get("MAX_B_TN", "10")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Hello My Dear Friends â¤ï¸')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Choose Option Settings 
LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]


                           # Don't Remove Credit @VJ_Botz
                           # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
                           # Ask Doubt on telegram @KingVJ01


# Online Stream and Download
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://cognitive-betteann-namanrathoreji-3d58d83f.koyeb.app/")


# Rename Info : If True Then Bot Rename File Else Not
RENAME_MODE = bool(environ.get('RENAME_MODE', True)) # Set True or False

# Auto Approve Info : If True Then Bot Approve New Upcoming Join Request Else Not
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False)) # Set True or False

# Save Restricted Info : If True Then Bot Save Content From Restricted Channel Else Not
SAVE_RESTRICTED_MODE = bool(environ.get('SAVE_RESTRICTED_MODE', True)) # Set True or False

# if SAVE_RESTRICTED_MODE is True Then Fill String Session Variable In Your Server Environment Variable, If Flase Then No Need To Fill.
# Warning: Never Fill String Session Variable In Your Repo, If You Fill Then Your Account Can Be Access By Anyone.
SESSION_STRING = environ.get('SESSION_STRING', '') # PYROGRAM V2 Session 

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
