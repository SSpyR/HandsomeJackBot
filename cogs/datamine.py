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
            

    @commands.command(name='ref', help='Command for searching through the in-game files, auto-directs to bot specific chat')
    async def bl_ref(self, ctx, *, queryname: str):
        destchat=None
        fileFolder='/home/sspyr/BL3/FoundFiles'

        for channel in ctx.guild.channels:
            if channel.name=='handsome-jackbot':
                destchat=channel
        if destchat==None:
            await ctx.send('handsome-jackbot channel not detected and is required.')

        if os.path.isdir(fileFolder):
            await destchat.send('{}'.format(ctx.author.mention))
            await destchat.send('```RESULTS```')
            queryname=queryname.replace(' ', '_')
            for root, dirs, files in os.walk(fileFolder):
                for name in files:
                    if (queryname.lower() in name.lower()) and name.endswith('.json'):
                        response=os.path.join(root, name)
                        await destchat.send('```{}```'.format(response.replace('lavoiet2', 'USER')))
            await destchat.send('```SEARCH DONE```')
        else:
            print ('Directory Not Found')           


    @bl_ref.error
    async def bl_ref_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('{} ref command requires a query name to search for.'.format(ctx.author.mention))


    @commands.command(name='refget', help='Command for displaying in-game files, must enter full file name (does not require caps or ".json"), auto-directs to bot specific chat')
    async def bl_refget(self, ctx, *, filename: str):
        destchat=None
        fileFolder='/home/sspyr/BL3/FoundFiles'

        for channel in ctx.guild.channels:
            if channel.name=='handsome-jackbot':
                destchat=channel
        if destchat==None:
            await ctx.send('handsome-jackbot channel not detected and is required.')
        
        if os.path.isdir(fileFolder):
            await destchat.send('{}'.format(ctx.author.mention))
            fileSent=False
            if ('.json' not in filename.lower()):
                filename+='.json'
            for root, dirs, files in os.walk(fileFolder):
                for name in files:
                    if (filename.lower()==name.lower()):
                        target=os.path.join(root, name)
                        await destchat.send(file=discord.File(target))
                        fileSent=True
            if fileSent==False:
                await destchat.send('```{} Could Not Be Found.```'.format(filename))            
        else:
            print ('Directory Not Found')        


    @bl_refget.error
    async def bl_refget_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('{} refget command requires a file name to search for.'.format(ctx.author.mention))
        

def setup(bot):
    bot.add_cog(Datamine(bot))
