# bot.py

import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

startup_extensions=['resources', 'social', 'datamine', 'hotfix']
token = os.getenv('DISCORD_TOKEN')
owner_id = os.getenv('OWNER_ID')
bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print('\n')
    print('Discord: Successfully Connected As:')
    print(bot.user.name)
    print('<',bot.user.id,'>')

    print('\n')
    print('Bot Owned By:')
    print('SSpyR')
    print('<',owner_id,'>')

    activity=discord.Activity(name='for Randy', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


@bot.command
@bot.is_owner
async def load(ctx, extension_name : str):
    try:
        bot.load_extension(extension_name)
    except Exception as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))


@bot.command
@bot.is_owner
async def unload(ctx, extension_name : str):
    bot.unload_extension(extension_name)
    await ctx.send("{} unloaded.".format(extension_name))


@bot.command(name='shutdown')
async def shutdown(ctx):
    if ctx.author.id==int(owner_id):
        await ctx.send('Shutting Down...')
        print('Shutdown Command Executed by Owner')
        await bot.logout()
    else:
        print (type(ctx.author.id),'{}'.format(ctx.author.id))
        print (type(owner_id),owner_id)
        print('Shutdown Command Execution Attempted by Non-Owner')


if __name__=="__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exception='{}: {}'.format(type(e).__name__, e)
            print('Extension could not be loaded {}\n{}'.format(extension,exception))
    
    bot.run(token)






