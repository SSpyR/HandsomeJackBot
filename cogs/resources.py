# resources.py

import os
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import csv

from discord_slash.utils.manage_commands import create_option
from bot import officialServerID, jackbotChatID, invincibleRoleID, ccRoleID, tubbyRoleID, badassRoleID

class Resources(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    #@commands.command(name='bl3builds', help='Google Docs of Borderlands 3 Builds, Updated to Current Content')
    @cog_ext.cog_slash(name='bl3builds', description='Google Docs of Borderlands 3 Builds, Updated to Current Content')
    async def bl3_builds(self, ctx: SlashContext):
        response=':purple_heart:[Amara Builds](https://docs.google.com/document/d/1rpIwTi2hrWywgB42_I2mCjLqZ72r-n1FAoA2w8LGoGA/edit?usp=sharing>) \n \n'
        response+=':green_heart:[FL4K Builds](https://docs.google.com/document/d/1MiGGa_HDpm_IzHWgfhIDkLxzqiL_7O5HRC8E8ICerQg/edit?usp=sharing>) \n \n'
        response+=':heart:[Moze Builds](https://docs.google.com/document/d/1hLiqOQ3PcA2oPVqaXuq2cU09EvLwoZx2KADgP6GwZ1A/edit>) \n \n' 
        response+=':yellow_heart:[Zane Builds](https://docs.google.com/document/d/1p9tA92kJx2ZOKJG8r7G2yEQi6XE9p8qjlWvJWoNgfu4/edit?usp=sharing>)'
        embed=discord.Embed(
            title='BL3 Build Compendiums',
            description=response,
            color=discord.Color.dark_gold()
        )
        embed.set_footer(text='')
        embed.add_field(name='\u200B', value='[Submit a Build Here](https://docs.google.com/forms/d/e/1FAIpQLSe_RkUKIvzHoRXlHgQh4TnERgQK6H-yXW2RJkUmn7sFUn4x0Q/viewform)', inline=True)
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID):
                return
            perms=False
            await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(tubbyRoleID):
                perms=True
            if perms==True:
                await officialguild.get_channel(jackbotChatID).send(embed=embed)
            else:
                await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.send(embed=embed)


    #@commands.command(name='bl3info', help='Various Useful Links for BL3')
    @cog_ext.cog_slash(name='bl3info', description='Various Useful Links for BL3')
    async def bl3_info(self, ctx: SlashContext):
        response='[BL3 Formulas Document](https://docs.google.com/document/d/1pnBcjHF3OuRItROdUPdBGw3vwC7v_5CB2pdJzj5wsb0/edit?usp=sharing) \n'
        response+='[BL3 Splash Damage & Anoint Forum Post](https://forums.gearboxsoftware.com/t/list-of-all-splash-weapons/4399732) \n'
        response+='[BL3 Endgame Guide](https://docs.google.com/document/d/1JLHVuD7AdCA5TwQxCahgbbiZHbkyFOXh6uZZjPlTBAU/edit) \n'
        response+='[BL3 Loot Information](https://www.lootlemon.com/) \n'
        response+='[BL3 Save Editor](https://github.com/cfi2017/bl3-save) \n'
        response+='[BL3 Modding](https://www.nexusmods.com/borderlands3/mods/244) \n'
        embed=discord.Embed(
            title='BL3 Useful Links',
            description=response,
            color=discord.Color.dark_teal()
        )
        embed.set_footer(text='')
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID):
                return
            perms=False
            await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(tubbyRoleID):
                perms=True
            if perms==True:
                await officialguild.get_channel(jackbotChatID).send(embed=embed)
            else:
                await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.send(embed=embed)


    #@commands.command(name='math', help='Formula Sheet for all of the Vault Hunters')
    #async def bl_math(self, ctx):
    #    response='https://docs.google.com/document/d/1pnBcjHF3OuRItROdUPdBGw3vwC7v_5CB2pdJzj5wsb0/edit?usp=sharing'
    #    await ctx.send(response)


    #@commands.command(name='splash', help='Forum Post for Tracking Splash Weapon Damage Information')
    #async def bl_splash(self, ctx):
    #    response='https://forums.gearboxsoftware.com/t/list-of-all-splash-weapons/4399732'
    #    await ctx.send(response)

    
    #@commands.command(name='itemeditor', help='Web-based Item Editor for Borderlands 3. Courtesy of Baysix')
    #async def bl_itemedit(self, ctx):
    #    response='Courtesy of Baysix: https://www.bl3editor.com/#/'
    #    await ctx.send(response)


    #@commands.command(name='bl3drop', help='Website for Drop Rates, Locations. and many more of BL3 Unique Items. Courtesy of Levin')
    #async def bl_bl3drop(self, ctx):
    #    response='Find Drop Rates and Locations Here: https://www.lootlemon.com/'
    #    await ctx.send(response)

        
    #@commands.command(name='bl3modding', help='Nexus Mods Page for the BL3 Hotfix Merger. Courtesy of c0dycode')
    #async def bl_bl3modding(self, ctx):
    #    response='Get Started with BL3 Hotfix Modding Here: https://www.nexusmods.com/borderlands3/mods/244'
    #    await ctx.send(response)


    #@commands.command(name='bl3files', help='Links to the Nexus Mods Page of Serialized Game Files. Courtesy of Grimm')
    @cog_ext.cog_slash(name='bl3files', description='Links to the Nexus Mods Page of Serialized Game Files. Courtesy of Grimm')
    async def database(self, ctx: SlashContext):
        embed=discord.Embed(
            title='BL3 Serialized Game Files',
            description='[Nexus Mod Page Link](https://www.nexusmods.com/borderlands3/mods/247)',
            color=discord.Color.dark_green()
        )
        embed.set_footer(text='Courtesy of Grimm')
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID):
                return
            perms=False
            await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(tubbyRoleID):
                perms=True
            if perms==True:
                await officialguild.get_channel(jackbotChatID).send(embed=embed)
            else:
                await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.channel.send(embed=embed)


    #TODO Edit Agonizer rates for various Mayhem Levels
    #@commands.command(name='dropinfo', help='Search Command for Finding the Drop Rate and Location of an Item')
    @cog_ext.cog_slash(name='dropinfo', description='Search Command for Finding the Drop Rate and Location of an Item', options=[create_option(name='queryname', description='Name of Item to Search For', option_type=3, required=True)])
    async def bl_droprate(self, ctx: SlashContext, queryname: str):
        officialguild=self.bot.get_guild(officialServerID)
        perms=True
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID):
                return
            perms=False
            await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(tubbyRoleID):
                perms=True
            if perms==False:
                await officialguild.get_channel(jackbotChatID).send('Oops! You do not have the proper permissions for that.')
        if perms==True:
            found=False
            embed=None
            name=''
            itemtype='weapon'
            lootlemon=''
            dir=os.path.dirname(__file__)
            with open(os.path.join(dir, 'utils/droprates.csv'), newline='') as csvfile:
                lreader=csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in lreader:
                    response=''
                    queryname=queryname.replace("'","")
                    if 'pat' in queryname.lower():
                        queryname='p.a.t'
                    if 'o.p.q.' in queryname.lower():
                        queryname='opq'
                    if queryname.lower() in row[0].lower():
                        name=row[0]
                        response+="Drop Source: "+row[2]
                        if row[4]!='':
                            response+="\nDrop Rate/Notes: "+row[3]+" ("+row[4]+")"
                        else:
                            response+="\nDrop Rate/Notes: "+row[3]
                        if "grenade mod" in row[1].lower():
                            itemtype='grenade-mod'
                        elif "class mod" in row[1].lower():
                            itemtype='class-mod'
                        elif "shield" in row[1].lower():
                            itemtype='shield'
                        elif "artifact" in row[1].lower():
                            itemtype='bonus-item'
                        linkname=name.lower()
                        if 'seventh sense' in linkname:
                            linkname='seventh sense legendary'
                        linkname=linkname.replace(' ', '-')
                        linkname=linkname.replace('.','-')
                        lootlemon='https://lootlemon.com/{}/{}-bl3'.format(itemtype, linkname)
                        embed=discord.Embed(
                            title='Drop Info for {}'.format(name),
                            description=response,
                            color=discord.Color.purple()
                        )
                        embed.add_field(name='\u200B', value='[Further Information on Lootlemon]({})'.format(lootlemon), inline=True)
                        if ctx.guild==officialguild:
                            await officialguild.get_channel(jackbotChatID).send(embed=embed)
                            if name.lower()=='bearcat':
                                await officialguild.get_channel(jackbotChatID).send(':pray:')
                            found=True
                        else:
                            await ctx.send(embed=embed)
                            if name.lower()=='bearcat':
                                await ctx.send(':pray:')
                            found=True
                if found==False:
                    await ctx.send('No Item with Name {} could be found.'.format(queryname))
        

def setup(bot):
    bot.add_cog(Resources(bot))