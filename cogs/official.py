# official.py

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import random

from discord_slash.utils.manage_commands import create_option
from bot import officialServerID, jackbotChatID, invincibleRoleID, ccRoleID, tubbyRoleID, badassRoleID

class Official(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    #@commands.command(name='hotfixes')
    @cog_ext.cog_slash(name='hotfixes', description='Helpful Information About BL3 Hotfixes', guild_ids=[officialServerID])
    async def bl3_hotfixes(self, ctx: SlashContext):
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send('If you\'re seeing unusual stats on your gear (incorrect values, incorrect rarities) or experiencing bugs that have been fixed according to patch notes, you may not have let hotfixes apply. To let them apply go to the main menu and wait for the "Hotfixes Applied" sign to appear. You must be online for this to happen and it can take anywhere between 5 seconds to a minute depending on your connection strength')
            # await officialguild.get_channel(jackbotChatID).send('If you\'re seeing unusual stats on your gear (incorrect values, incorrect rarities) or experiencing bugs that have been fixed according to patch notes, you may not have let hotfixes apply. To let them apply go to the main menu and wait for the "Hotfixes Applied" sign to appear. You must be online for this to happen and it can take anywhere between 5 seconds to a minute depending on your connection strength')
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='lfg')
    @cog_ext.cog_slash(name='lfg', description='LFG Redirection Message', guild_ids=[officialServerID], options=[create_option(name='user', description='Specific User to Mention with Message', option_type=6, required=False)])
    async def lfg(self, ctx: SlashContext, user: discord.User=None):
        response='If you plan to play, boost, or trade with someone, please read <#574884110904852480> to get set up! This channel has all the information you\'ll need about our LFG channels! Getting started is as simple as assigning yourself a platform role in <#548843527082213376>! Enjoy yourselves Vault Hunters!'
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            if user is None:
                await ctx.send(response)
                # await officialguild.get_channel(jackbotChatID).send(response)
                #await ctx.message.delete()
            else:
                response=str(user.mention)+'\n'+response
                await ctx.send(response)
                # await officialguild.get_channel(jackbotChatID).send(response)
                #await ctx.message.delete()
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='support')
    @cog_ext.cog_slash(name='support', description='Links to Gearbox and 2K Support Resources', guild_ids=[officialServerID])
    async def support(self, ctx: SlashContext):
        response='If you\'re looking for help with any of your game related issues, here are the official support links you may need:\n' 
        response+='Gearbox Contact: <https://www.gearboxsoftware.com/contact/>\n'
        response+='Gearbox Software Support: <https://gearboxsoftware.zendesk.com/hc/en-us>\n'
        response+='2K Support: <https://support.2k.com/hc/en-us>\n'
        response+='Shift Support: <https://gearboxsoftware.zendesk.com/hc/en-us/sections/200939080-SHiFT>\n'
        response+='VIP Troubleshooting and Support:  <https://support.2k.com/hc/en-us/articles/360021095353-Vault-Insider-Program-VIP-FAQ>\n\n'
        response+='For platform support (Xbox, PlayStation, Epic Games, Stadia) please go to official platform support websites.'
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send(response)
            # await officialguild.get_channel(jackbotChatID).send(response)
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='splash')
    @cog_ext.cog_slash(name='splash', description='Resources on Splash Damage/Weapons for Various Games in the Series', guild_ids=[officialServerID])
    async def splash(self, ctx: SlashContext):
        response='**BL2:**\n<https://forums.gearboxsoftware.com/t/complete-splash-damage-guide/1553510>\n\n'
        response+='**BLTPS:**\n<https://forums.gearboxsoftware.com/t/complete-splash-damage-guide-tps-version/1558812>\n\n'
        response+='**BL3:**\n<https://forums.gearboxsoftware.com/t/list-of-all-splash-weapons/4399732>'
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send(response)
            # await officialguild.get_channel(jackbotChatID).send(response)
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='bl3who')
    @cog_ext.cog_slash(name='bl3who', description='Randomly Selects a VH to Say to Play', guild_ids=[officialServerID])
    async def bl3who(self, ctx: SlashContext):
        vhList=['Amara', 'Moze', 'Zane', 'FL4K']
        vhChoice=random.choice(vhList)
        response='You should play **{}**!'.format(vhChoice)
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send(response)
            # await officialguild.get_channel(jackbotChatID).send(response)
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='bl2who')
    @cog_ext.cog_slash(name='bl2who', description='Randomly Selects a VH to Say to Play', guild_ids=[officialServerID])
    async def bl2who(self, ctx: SlashContext):
        vhList=['Axton', 'Zer0', 'Maya', 'Salvador', 'Gaige', 'Krieg']
        vhChoice=random.choice(vhList)
        response='You should play **{}**!'.format(vhChoice)
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send(response)
            # await officialguild.get_channel(jackbotChatID).send(response)
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='tpswho')
    @cog_ext.cog_slash(name='tpswho', description='Randomly Selects a VH to Say to Play', guild_ids=[officialServerID])
    async def bltpswho(self, ctx: SlashContext):
        vhList=['Athena', 'Wilhelm', 'Nisha', 'Claptrap', 'Jack', 'Aurelia']
        vhChoice=random.choice(vhList)
        response='You should play **{}**!'.format(vhChoice)
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send(response)
            # await officialguild.get_channel(jackbotChatID).send(response)
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='bl1who')
    @cog_ext.cog_slash(name='bl1who', description='Randomly Selects a VH to Say to Play', guild_ids=[officialServerID])
    async def bl1who(self, ctx: SlashContext):
        vhList=['Mordecai', 'Roland', 'Lilith', 'Brick']
        vhChoice=random.choice(vhList)
        response='You should play **{}**!'.format(vhChoice)
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send(response)
            # await officialguild.get_channel(jackbotChatID).send(response)
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


    #@commands.command(name='event')
    @cog_ext.cog_slash(name='event', description='Helpful Information About BL3 Events', guild_ids=[officialServerID])
    async def bl3_event(self, ctx: SlashContext):
        perms=False
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild!=officialguild:
            return
        # if ctx.channel!=officialguild.get_channel(jackbotChatID):
        #     return
        # await ctx.send('Request Retrieved')
        if ctx.author.top_role>=officialguild.get_role(badassRoleID):
            perms=True
        if perms==True:
            await ctx.send('In order to activate any event (Cartels, Broken Hearts or Bloody Harvest) go to main menu, click play and new option will show up on the bottom of menu to enable it')
            # await officialguild.get_channel(jackbotChatID).send('In order to activate any event (Cartels, Broken Hearts or Bloody Harvest) go to main menu, click play and new option will show up on the bottom of menu to enable it')
        else:
            await ctx.send('Oops! You do not have the proper permissions for that.')
            # await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')


def setup(bot):
    bot.add_cog(Official(bot))