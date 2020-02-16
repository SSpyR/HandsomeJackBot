# social.py

# look at mee6 bot to see how they get twitter updates to post (for keeping us up to date on randy)

import discord
from discord.ext import commands

class Social(commands.Cog):

    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='invite', help='Invite Link for the Bot')
    async def server_invite(self, ctx):
        response='https://discordapp.com/api/oauth2/authorize?client_id=660646451273007127&permissions=8&scope=bot'
        await ctx.send('{} A Direct Message has Been Sent You.'.format(ctx.author.mention))
        await ctx.author.send('Here is the link to invite Handsome JackBot to your Discord. Make sure to grant it Admin privileges.')
        await ctx.author.send(response)

    
    @commands.command(name='tutorial', help='Tutorial Video for the Bot')
    async def video_link(self, ctx):
        response='https://youtu.be/rTVcSizSIQQ'
        await ctx.send(response)


    @commands.command(name='github', help='Github Repository for the Bot')
    async def github_link(self, ctx):
        response='https://github.com/SSpyR/HandsomeJackBot.git'
        await ctx.send('{} A Direct Message has Been Sent You.'.format(ctx.author.mention))
        await ctx.author.send('Here is the link to the Github Repo.')
        await ctx.author.send(response)


    @commands.command(name='randy', help='Randy Emote')
    async def bl_randy(self, ctx):
        response='<:justintime:646748813981384746>'
        await ctx.send(response)


    @commands.command(name='channel', help='Creates the Handsome JackBot Channel')
    async def channel_create(self, ctx):
        channel=False
        if 'handsome-jackbot' in ctx.guild.text_channels:
            channel=True
        try:
            if channel==False:
                await ctx.guild.create_text_channel('handsome-jackbot')
                await ctx.send('Channel Created.')
            else:
                await ctx.send('Channel Already Exists.')
        except discord.errors.Forbidden:
            await ctx.send('Missing Permissions.')


    @commands.Cog.listener()
    async def on_message(self, message):
        guild=self.bot.get_guild(632633098584064018)

        if message.author==self.bot.user:
            return
        
        if message.guild==guild:
            if 'randy' in message.content:
                response='<:justintime:646748813981384746>'
                await message.channel.send(response)
            if 'RANDY' in message.content:
                response='<:4hed:662477280034947072>'
                await message.channel.send(response)


def setup(bot):
    bot.add_cog(Social(bot))
