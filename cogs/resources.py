# resources.py


import discord
from discord.ext import commands

class Resources(commands.Cog):

    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='builds', help='Imgur Album of Borderlands 3 Builds, Updated to Current Content')
    async def bl_builds(self, ctx):
        response='https://imgur.com/a/6yfA9oo'
        await ctx.send(response)


    @commands.command(name='archive', help='State of the Game for Borderlands 3, Updated on Every Major Patch')
    async def bl_archive(self, ctx):
        response='https://docs.google.com/document/d/13oknxW3ExtG-YoM8CTeeDgCrc4bVFcFhX6UsPftEM5s/edit?usp=sharing'
        await ctx.send(response)


    @commands.command(name='math', help='Formula Sheet for all of the Vault Hunters')
    async def bl_math(self, ctx):
        response='https://docs.google.com/document/d/1pnBcjHF3OuRItROdUPdBGw3vwC7v_5CB2pdJzj5wsb0/edit?usp=sharing'
        await ctx.send(response)
        

def setup(bot):
    bot.add_cog(Resources(bot))