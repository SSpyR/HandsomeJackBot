# datamine.py

import os
import sys
import json
import appdirs
import requests
import datetime
import time
import discord

from discord.ext import commands


class Datamine(commands.Cog):

    def __init__(self, bot):
        self.bot=bot
            

    #@commands.command(name='ref', help='Command for searching through the in-game files, auto-directs to bot specific chat')
    #async def bl_ref(self, ctx, *, queryname: str):
    #    destchat=None
    #    fileFolder=''
    #
    #    for channel in ctx.guild.channels:
    #        if channel.name=='handsome-jackbot':
    #            destchat=channel
    #    if destchat==None:
    #        await ctx.send('handsome-jackbot channel not detected and is required.')
    #
    #    queryname=queryname.replace(' ', '_')
    #
    #    if os.path.isdir(fileFolder):
    #        await destchat.send('{}'.format(ctx.author.mention))
    #        #await destchat.send('```Only Balance and PartSet Files Are Currently Availabe```')
    #        await destchat.send('```RESULTS```')
    #        queryname=queryname.replace(' ', '_')
    #        counter=0
    #        for root, dirs, files in os.walk(fileFolder):
    #            for name in files:
    #                if (queryname.lower() in name.lower()) and name.endswith('.json'):
    #                    response=os.path.join(root, name)
    #                    response=response.replace('\\', '/')
    #                    await destchat.send('```{}```'.format(response.replace('', '')))
    #                    counter+=1
    #                if counter >= 25:
    #                    break
    #            if counter >= 25:
    #                await destchat.send('```ONLY A MAXIMUM OF 25 QUERY RESULTS CAN BE DISPLAYED WITH ONE SEARCH```')
    #                break
    #        await destchat.send('```SEARCH DONE```')
    #    else:
    #        print ('Directory Not Found')    


    #@bl_ref.error
    #async def bl_ref_error(self, ctx, error):
    #    if isinstance(error, commands.MissingRequiredArgument):
    #        await ctx.send('{} ref command requires a query name to search for.'.format(ctx.author.mention))


    #@commands.command(name='refget', help='Command for displaying in-game files, must enter full file name (does not require caps or ".json"), auto-directs to bot specific chat')
    #async def bl_refget(self, ctx, *, filename: str):
    #    destchat=None
    #    fileFolder=''
    #
    #    for channel in ctx.guild.channels:
    #        if channel.name=='handsome-jackbot':
    #            destchat=channel
    #    if destchat==None:
    #        await ctx.send('handsome-jackbot channel not detected and is required.')
    #    
    #    if os.path.isdir(fileFolder):
    #        await destchat.send('{}'.format(ctx.author.mention))
    #        fileSent=False
    #        if ('.json' not in filename.lower()):
    #            filename+='.json'
    #        for root, dirs, files in os.walk(fileFolder):
    #            for name in files:
    #                if (filename.lower()==name.lower()):
    #                    target=os.path.join(root, name)
    #                    await destchat.send(file=discord.File(target))
    #                    fileSent=True
    #        if fileSent==False:
    #            await destchat.send('```{} Could Not Be Found.```'.format(filename))            
    #    else:
    #        print ('Directory Not Found')        


    #@bl_refget.error
    #async def bl_refget_error(self, ctx, error):
    #    if isinstance(error, commands.MissingRequiredArgument):
    #        await ctx.send('{} refget command requires a file name to search for.'.format(ctx.author.mention))

    
    #@commands.command(name='helperapp', help='Links to Stand-Alone BL3 Editor Helper App')
    #async def helperapp(self, ctx):
    #    response='https://github.com/SSpyR/BL3EditorHelper'
    #    await ctx.channel.send(response)


    #@commands.command(name='database', help='Links to Personal Google Drive Storage of Game Files')
    #async def database(self, ctx):
    #    await ctx.channel.send('Nexus Mods Page of Serialized Game Files')
    #    response='https://www.nexusmods.com/borderlands3/mods/247'
    #    await ctx.channel.send(response)


def setup(bot):
    bot.add_cog(Datamine(bot))
