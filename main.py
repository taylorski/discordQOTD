# django initial stuff
import os

# Django specific settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application

# Ensure settings are read
application = get_wsgi_application()

# discord.py stuff
from discord.ext.commands import Bot

# library stuff
import json
import os
import sys
import traceback
# local
from discord_handler.cogs import *
from db.models import Error,DBGuild
from discord_handler.meta import get_pre
from BBase.log_handler.loghandler import setup_logging
from BBase.discord.bot_pages.cog_discordbots import discordbot_update
setup_logging()

bot = Bot(command_prefix=get_pre)
path = os.path.dirname(os.path.realpath(__file__)) + "/"

@bot.event
async def on_error(event, *args, **kwargs):
    try:
        g = DBGuild.objects.get(id=args[0].guild.id)
    except DBGuild.DoesNotExist:
        g = DBGuild(id=args[0].guild.id,name=args[0].guild.name)
        g.save()
    except IndexError:
        return
    sys_info = sys.exc_info()
    e = Error(g=g, cmd_string=event
              , error_type=f'{sys_info[0]}', error=f'{sys_info[1]}', traceback=traceback.format_exc())
    e.save()
    bot_owner = bot.get_cog('BotOwner')
    await bot_owner.send_error_notification(e, args[0].guild)

bot.add_cog(All(bot))
bot.add_cog(Owner(bot))
bot.add_cog(Setup(bot))
bot.add_cog(QuestionCmd(bot))
bot.add_cog(AnswerCmd(bot))
bot.add_cog(Mod(bot))

with open(f'{path}secret.json', 'r') as f:
    d = json.load(f)
bot.add_cog(BotOwner(bot,d))
discordbot_update(bot,d)
bot.run(d['discord_secret'])
