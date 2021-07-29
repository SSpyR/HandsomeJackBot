# bot.py
# Creator: SSpyR

#TODO Update with link to Announcements Server
#TODO Do BL2 & TPS stuff?
#TODO Add auto randy emote to Official but locked behind invinc and up
#TODO Pins Command for Official with how to Check Pins (see Frank Command)
#TODO Get rid of help command

## Test Bot Invite Link: https://discord.com/api/oauth2/authorize?client_id=723253848898273380&permissions=2147532800&scope=bot%20applications.commands

## OFFICIAL IDS
## INVINCIBLE: 561841778395840523
## CONTENT CREATOR: 790139584025591819
## TUBBY: 464235639584587787
## BADASS: 453875267782443010
## RABID: 453875169207910406

import os
import discord
import logging
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv

dotenv_path=os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
logging.basicConfig(level=logging.INFO)

startup_extensions=['cogs.resources', 'cogs.social', 'cogs.hotfix', 'cogs.official'] #, 'cogs.official' <- put back in before shipping
#['cogs.resources', 'cogs.social', 'cogs.hotfix'] #, 'cogs.hotfix' keep out while testing and fixing
token=os.getenv('DISCORD_TOKEN')
owner_id=os.getenv('OWNER_ID')
bot=commands.Bot(command_prefix='~')
slash=SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

officialServerID=132671445376565248
jackbotChatID=860249638531498004
bl3ChatID=560903030137159711
bl3BuildsChatID=614575671884251141
bl3LootChatID=618688011009261568
invincibleRoleID=561841778395840523
ccRoleID=790139584025591819
tubbyRoleID=464235639584587787
badassRoleID=453875267782443010
rabidRoleID=453875169207910406

##Dont need if using slash commands
# class helpCommand(commands.MinimalHelpCommand):
#     def add_bot_commands_formatting(self, commands, heading):
#             if commands:
#                 if 'Official' not in str(heading):
#                     # U+2002 Middle Dot
#                     joined = '\u2002'.join(c.name for c in commands)
#                     self.paginator.add_line('__**%s**__' % heading)
#                     self.paginator.add_line(joined)
#     async def send_pages(self):
#         dest=None
#         officialguild=bot.get_guild(officialServerID)
#         if self.context.guild==officialguild:
#             if self.context.channel!=officialguild.get_channel(jackbotChatID):
#                 return
#             dest=officialguild.get_channel(jackbotChatID)
#         else:
#             dest=self.get_destination()
#         embed=discord.Embed(
#             color=discord.Color.blurple(),
#             description=''
#         )
#         print(self.paginator.pages)
#         for page in self.paginator.pages:
#             embed.description+=page
        
#         await dest.send(embed=embed)


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

    activity=discord.Activity(name='for Hotfixes', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


#bot.help_command=helpCommand()


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


#@bot.command(name='prune', help='only usable by owner')
#@bot.is_owner
#async def blprune(ctx):
#    official=bot.get_guild(132671445376565248)
#    if ctx.author.id==int(owner_id) and ctx.guild==official:
#        for channel in ctx.guild:
#            if channel.name=="join-leave-log":
#                for message in channel.history(limit=2000):
#                    if message.content.contains('bailo'):
#                        print('found')
#    else:
#        await ctx.send('permission denied to perform this command')


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





