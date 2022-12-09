# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -100))
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/MdiskLinksSearchBot'>MdiskLinksSearchBot</a> is an open source project.

    Devs: 
        <a href='https://t.me/sigma_male_007'>❤️ PyroDeveloper ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Serve: <a href='https://heroku.com'>Microsoft Azure</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Main Channel: <a href='https://t.me/z_harbour'>Z_Harbour</a></b>
"""

    ABOUT_HELP_TEXT = """<b>❤️Developer❤️ : <a href='https://t.me/sigma_male_007'>PyroDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>I am Started Dear! {}😙,



Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You For Operating Me<a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Dear! {}😘,

I'm the one and only fastest URL & Movies-Series Links finder BOT On TG. Add me to any Group and Give me Operating rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Operating Dear {} </b> ««««


🔺 Thank You 🔺 
"""

