# resources.py

import os
import discord
from discord.ext import commands
import csv

class Resources(commands.Cog):

    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='builds', help='Google Docs of Borderlands 3 Builds, Updated to Current Content')
    async def bl_builds(self, ctx):
        response='**Amara Builds:** <https://docs.google.com/document/d/1rpIwTi2hrWywgB42_I2mCjLqZ72r-n1FAoA2w8LGoGA/edit?usp=sharing> \n \n'
        response+='**FL4K Builds:** <https://docs.google.com/document/d/1MiGGa_HDpm_IzHWgfhIDkLxzqiL_7O5HRC8E8ICerQg/edit?usp=sharing> \n \n'
        response+='**Moze Builds:** <https://docs.google.com/document/d/10nJUJxvTmYP4k8bOrb_FaVVdouozwiqAZ0A-EzIENMo/edit?usp=sharing> \n \n' 
        response+='**Zane Builds:** <https://docs.google.com/document/d/1p9tA92kJx2ZOKJG8r7G2yEQi6XE9p8qjlWvJWoNgfu4/edit?usp=sharing>'
        await ctx.send(response)


    #@commands.command(name='archive', help='State of the Game for Borderlands 3, Updated on Every Major Patch')
    #async def bl_archive(self, ctx):
    #    response='https://docs.google.com/document/d/13oknxW3ExtG-YoM8CTeeDgCrc4bVFcFhX6UsPftEM5s/edit?usp=sharing'
    #    await ctx.send(response)


    @commands.command(name='math', help='Formula Sheet for all of the Vault Hunters')
    async def bl_math(self, ctx):
        response='https://docs.google.com/document/d/1pnBcjHF3OuRItROdUPdBGw3vwC7v_5CB2pdJzj5wsb0/edit?usp=sharing'
        await ctx.send(response)


    @commands.command(name='splash', help='Forum Post for Tracking Splash Weapon Damage Information')
    async def bl_splash(self, ctx):
        response='https://forums.gearboxsoftware.com/t/list-of-all-splash-weapons/4399732'
        await ctx.send(response)

    
    @commands.command(name='itemeditor', help='Web-based Item Editor for Borderlands 3, Courtesy of Baysix')
    async def bl_itemedit(self, ctx):
        response='Courtesy of Baysix: https://www.bl3editor.com/#/'
        await ctx.send(response)


    @commands.command(name='bl3drop', help='Spreadsheet for Drop Rates of BL3 Unique Items')
    async def bl_bl3drop(self, ctx):
        response='Drop Rate Table: <https://docs.google.com/spreadsheets/d/e/2PACX-1vRUVAWx2LtfOENd61Xt_PJl95Qn0r1nhAGjwHCUnh3YZ_kWSN7xjgs9INgKjxGTA7Ug-odHRddUXRZP/pubhtml#>'
        await ctx.send(response)


    @commands.command(name='dropinfo', help='Search Command for Finding the Drop Rate and Location of an Item')
    async def bl_droprate(self, ctx, *, queryname: str):
        response=''
        name=''
        dir=os.path.dirname(__file__)
        with open(os.path.join(dir, 'utils/droplocations.csv'), newline='') as csvfile:
            with open(os.path.join(dir, 'utils/droprates.csv'), newline='') as csvfile2:
                lreader=csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in lreader:
                    if len(row) > 6:
                        if queryname.lower() in row[2].lower():
                            name=row[2]
                            if row[6] == "TRUE" or row[6] == "" and row[7] != "":
                                response+="**Drop Location for {}:** ".format(name)+row[7]+" ("+row[9]+")"
                            elif row[8] == "":
                                response+="**Drop Location for {}:** ".format(name)+row[7]+" ("+row[9]+")"
                            else:
                                response+="**Drop Location for {}:** ".format(name)+row[6]+" ("+row[9]+")"
                rreader=csv.reader(csvfile2, delimiter=',', quotechar='|')
                for row2 in rreader:
                    if queryname.lower() in row2[0].lower():
                        response+="\n**Drop Rate and Notes for {}:** ".format(name)+row2[2]+" ("+row2[3]+")"
        await ctx.send(response)
        

def setup(bot):
    bot.add_cog(Resources(bot))