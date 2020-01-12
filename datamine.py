# datamine.py

# simplify chat and guild variables if possible

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
        guild1=self.bot.get_guild(632633098584064018)
        guild2=self.bot.get_guild(639786657666826242)
        guild3=self.bot.get_guild(648588069250793492)
        chat1=self.bot.get_channel(661350189696811094)
        chat2=self.bot.get_channel(661363999656640513)
        chat3=self.bot.get_channel(664940635236728832)
        destchat=None
        fileFolder='C:\\Users\\lavoiet2\\Downloads\\BL3\\Datamining\\FoundFiles'
        if ctx.guild==guild1:
            destchat=chat1
        elif ctx.guild==guild2:
            destchat=chat2
        elif ctx.guild==guild3:
            destchat=chat3
        elif destchat is None:
            print('Chat Error')

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


    @commands.command(name='refget', help='Command for displaying in-game files, must enter full file name, auto-directs to bot specific chat')
    async def bl_refget(self, ctx, *, filename: str):
        guild1=self.bot.get_guild(632633098584064018)
        guild2=self.bot.get_guild(639786657666826242)
        guild3=self.bot.get_guild(648588069250793492)
        chat1=self.bot.get_channel(661350189696811094)
        chat2=self.bot.get_channel(661363999656640513)
        chat3=self.bot.get_channel(664940635236728832)
        destchat=None
        fileFolder='C:\\Users\\lavoiet2\\Downloads\\BL3\\Datamining\\FoundFiles'
        if ctx.guild==guild1:
            destchat=chat1
        elif ctx.guild==guild2:
            destchat=chat2
        elif ctx.guild==guild3:
            destchat=chat3
        elif destchat is None:
            print('Chat Error')
        
        if os.path.isdir(fileFolder):
            await destchat.send('{}'.format(ctx.author.mention))
            filename+='.json'
            for root, dirs, files in os.walk(fileFolder):
                for name in files:
                    if (filename.lower()==name.lower()):
                        target=os.path.join(root, name)
                        await destchat.send(file=discord.File(target))
        else:
            print ('Directory Not Found')        


    @bl_refget.error
    async def bl_refget_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('{} refget command requires a file name to search for.'.format(ctx.author.mention))
        

def setup(bot):
    bot.add_cog(Datamine(bot))