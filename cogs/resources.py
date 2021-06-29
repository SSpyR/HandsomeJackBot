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

    
    @commands.command(name='itemeditor', help='Web-based Item Editor for Borderlands 3. Courtesy of Baysix')
    async def bl_itemedit(self, ctx):
        response='Courtesy of Baysix: https://www.bl3editor.com/#/'
        await ctx.send(response)


    #@commands.command(name='bl3drop', help='Website for Drop Rates, Locations. and many more of BL3 Unique Items. Courtesy of Levin')
    #async def bl_bl3drop(self, ctx):
    #    response='Find Drop Rates and Locations Here: https://www.lootlemon.com/'
    #    await ctx.send(response)

        
    @commands.command(name='bl3modding', help='Nexus Mods Page for the BL3 Hotfix Merger. Courtesy of c0dycode')
    async def bl_bl3modding(self, ctx):
        response='Get Started with BL3 Hotfix Modding Here: https://www.nexusmods.com/borderlands3/mods/244'
        await ctx.send(response)


    @commands.command(name='database', help='Links to the Nexus Mods Page of Serialized Game Files. Courtesy of Grimm')
    async def database(self, ctx):
        await ctx.channel.send('Nexus Mods Page of Serialized Game Files')
        response='https://www.nexusmods.com/borderlands3/mods/247'
        await ctx.channel.send(response)


    @commands.command(name='dropinfo', help='Search Command for Finding the Drop Rate and Location of an Item')
    async def bl_droprate(self, ctx, *, queryname: str):
        found=False
        embed=None
        response=''
        name=''
        itemtype='weapon'
        lootlemon=''
        dir=os.path.dirname(__file__)
        with open(os.path.join(dir, 'utils/droprates.csv'), newline='') as csvfile:
            lreader=csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in lreader:
                queryname=queryname.replace("'","")
                if found is False:
                    if queryname.lower() in row[0].lower():
                        name=row[0]
                        response+="Drop Location for {}: ".format(name)+row[2]
                        response+="\nDrop Rate and Notes for {}: ".format(name)+row[3]+" ("+row[4]+")"
                        if "grenade mod" in row[1].lower():
                            itemtype='grenade-mod'
                        elif "class mod" in row[1].lower():
                            itemtype='class-mod'
                        elif "shield" in row[1].lower():
                            itemtype='shield'
                        elif "artifact" in row[1].lower():
                            itemtype='bonus-item'
                        linkname=name.lower()
                        linkname=linkname.replace(' ', '-')
                        lootlemon='https://lootlemon.com/{}/{}-bl3'.format(itemtype, linkname)
                        embed=discord.Embed(
                            title='Drop Info for {}'.format(name),
                            description=response,
                            color=discord.Color.blue()
                        )
                        embed.set_footer(text='Further Information Provided by Levin from Lootlemon')
                        embed.set_author(name='Handsome JackBot')
                        embed.add_field(name='Link to Lootlemon Page for More Info', value=lootlemon, inline=True)
                        found=True
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Resources(bot))