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
        if 'handsome-jackbot' in ctx.guild.channels:
            channel=True
        if ctx.message.author.guild_permissions.administrator:
            try:
                if channel==False:
                    await ctx.guild.create_text_channel('handsome-jackbot')
                    await ctx.send('Channel Created.')
                else:
                    await ctx.send('Channel Already Exists.')
            except discord.errors.Forbidden:
                await ctx.send('Bot Missing Permissions.')
        else:
            await ctx.send('You Do Not Have Permission To Use That Command.')


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
            if 'fuck you' in message.content.lower():
                response='Nou <:ritsupunch:726145739306303539>'
                await message.channel.send(response)
            if 'randall' in message.content.lower():
                response='<:Randall:757085563214889011>'
                await message.channel.send(response)


    @commands.command(name='raid', help='Ignore this Dumb Meme')
    async def raid(self, ctx, *, name: str):
        lads=self.bot.get_guild(97342233241464832)
        bois=self.bot.get_guild(632633098584064018)

        if ctx.guild==lads or ctx.guild==bois:
            name=name.split(' ')
            name=name[0]
            await ctx.send("I've never been much of a mobile gamer, but, forget everything you think you know about mobile games because Raid Shadow Legends is one of the most ambitious RPG projects of 2019 has just been released and will change everything. Just look at the level of detail of these characters! If you use the code " + '"' + name + '"' + " you can start with 50,000 silver and join the Special Launch Tournament, and you better hurry because it's getting big fast! You can play for totally free with the link: raidshadowlegends.com/" + name)


    @raid.error
    async def raid_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('{} raid command requires a name to use (should do a mention for memes).'.format(ctx.author.mention))


def setup(bot):
    bot.add_cog(Social(bot))
