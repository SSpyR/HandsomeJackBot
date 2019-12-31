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
        await ctx.author.send('Here is the link to invite Handsome JackBot to your Discord.')
        await ctx.author.send(response)

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

def setup(bot):
    bot.add_cog(Social(bot))
