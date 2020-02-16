# bot.py
# Creator: SSpyR

import os
import discord
import logging
import math
from discord.ext import commands
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
logging.basicConfig(level=logging.INFO)

startup_extensions=['cogs.resources', 'cogs.social', 'cogs.datamine', 'cogs.hotfix', 'cogs.calcMain']
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


@bot.command(name='shutdown', help='Only Usable by Owner')
async def shutdown(ctx):
    if ctx.author.id==int(owner_id):
        await ctx.send('Shutting Down...')
        print('Shutdown Command Executed by Owner')
        await bot.logout()
    else:
        print (type(ctx.author.id),'{}'.format(ctx.author.id))
        print (type(owner_id),owner_id)
        print('Shutdown Command Execution Attempted by Non-Owner')


@bot.event
async def on_guild_join(guild):
    try:
        await guild.create_text_channel('handsome-jackbot')
    except discord.errors.Forbidden:
        print('Missing Permissions on Join')


@bot.command(name='echo', help='Only Usable by Owner')
async def echo(ctx):
    if ctx.author.id==int(owner_id):
        for guild in bot.guilds:
            for channel in guild.channels:
                if channel.name=="handsome-jackbot":
                    response=(ctx.message.content).replace(ctx.prefix,'').replace(ctx.command.name,'')
                    await channel.send(response)


if __name__=="__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exception='{}: {}'.format(type(e).__name__, e)
            print('Extension could not be loaded {}\n{}'.format(extension,exception))
    
    bot.run(token)






