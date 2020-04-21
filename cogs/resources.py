# resources.py

import discord
from discord.ext import commands

class Resources(commands.Cog):

    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='builds', help='Imgur Album of Borderlands 3 Builds, Updated to Current Content')
    async def bl_builds(self, ctx):
        response='**Amara Builds:** <https://docs.google.com/document/d/1rpIwTi2hrWywgB42_I2mCjLqZ72r-n1FAoA2w8LGoGA/edit?usp=sharing> \n \n'
        response+='**FL4K Builds:** <https://docs.google.com/document/d/1MiGGa_HDpm_IzHWgfhIDkLxzqiL_7O5HRC8E8ICerQg/edit?usp=sharing> \n \n'
        response+='**Moze Builds:** <https://docs.google.com/document/d/10nJUJxvTmYP4k8bOrb_FaVVdouozwiqAZ0A-EzIENMo/edit?usp=sharing> \n \n' 
        response+='**Zane Builds:** <https://docs.google.com/document/d/1p9tA92kJx2ZOKJG8r7G2yEQi6XE9p8qjlWvJWoNgfu4/edit?usp=sharing>'
        await ctx.send(response)


    @commands.command(name='archive', help='State of the Game for Borderlands 3, Updated on Every Major Patch')
    async def bl_archive(self, ctx):
        response='https://docs.google.com/document/d/13oknxW3ExtG-YoM8CTeeDgCrc4bVFcFhX6UsPftEM5s/edit?usp=sharing'
        await ctx.send(response)


    @commands.command(name='math', help='Formula Sheet for all of the Vault Hunters')
    async def bl_math(self, ctx):
        response='https://docs.google.com/document/d/1pnBcjHF3OuRItROdUPdBGw3vwC7v_5CB2pdJzj5wsb0/edit?usp=sharing'
        await ctx.send(response)


    @commands.command(name='splash', help='Forum Post for Tracking Splash Weapon Damage Information')
    async def bl_splash(self, ctx):
        response='https://forums.gearboxsoftware.com/t/list-of-all-splash-weapons/4399732'
        await ctx.send(response)
        

def setup(bot):
    bot.add_cog(Resources(bot))