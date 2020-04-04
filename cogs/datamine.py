# datamine.py

# pull from google drive instead?
# google drive option proving difficult, will just link for now, will have work it out later
# Google Drive: https://drive.google.com/drive/u/2/folders/12hivF6YFDncMIWw5RwYaV5u_ql-R3GqK
# AWS S3 instead?
# tempory solution of just partsets and balance files to send with heroku

import os
import sys
import json
import appdirs
import requests
import datetime
import time
import discord

from discord.ext import commands
'''from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth=GoogleAuth()
gauth.LocalWebserverAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile("mycreds.txt")

drive=GoogleDrive(gauth)'''

class Datamine(commands.Cog):

    def __init__(self, bot):
        self.bot=bot
            

    @commands.command(name='ref', help='Command for searching through the in-game files, auto-directs to bot specific chat')
    async def bl_ref(self, ctx, *, queryname: str):
        destchat=None
        fileFolder='/app/utils/Game'

        for channel in ctx.guild.channels:
            if channel.name=='handsome-jackbot':
                destchat=channel
        if destchat==None:
            await ctx.send('handsome-jackbot channel not detected and is required.')

        queryname=queryname.replace(' ', '_')

        if os.path.isdir(fileFolder):
            await destchat.send('{}'.format(ctx.author.mention))
            await destchat.send('```Only Balance and PartSet Files Are Currently Availabe```')
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
        fileFolder='/app/utils/Game'

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

    
    @commands.command(name='helperapp', help='Links to Stand-Alone BL3 Editor Helper App')
    async def helperapp(self, ctx):
        response='https://github.com/SSpyR/BL3EditorHelper'
        await ctx.channel.send(response)


    @commands.command(name='database', help='Links to Personal Google Drive Storage of Game Files (Temporary Solution to Full Ref)')
    async def database(self, ctx):
        await ctx.channel.send('Google Drive Folder of Game Files')
        response='https://drive.google.com/drive/u/2/folders/12hivF6YFDncMIWw5RwYaV5u_ql-R3GqK'
        await ctx.channel.send(response)


def setup(bot):
    bot.add_cog(Datamine(bot))
