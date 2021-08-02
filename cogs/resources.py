# resources.py

import os
import discord
import csv
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from bot import officialServerID, jackbotChatID, bl3ChatID, bl3BuildsChatID, bl3LootChatID, bl2ChatID, invincibleRoleID, ccRoleID, tubbyRoleID, badassRoleID, rabidRoleID

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
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl3ChatID) and ctx.channel!=officialguild.get_channel(bl3BuildsChatID) and ctx.channel!=officialguild.get_channel(bl3LootChatID):
                print('Hey you fucked up')
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(rabidRoleID):
                perms=True
            if perms==True:
                await ctx.send(embed=embed)
            else:
                await ctx.send('Oops! You do not have the proper permissions for that.')
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
        response+='[BL3 Max Damage Roll Sheet](https://docs.google.com/spreadsheets/d/1L-BU-n9gGdXvXl41RE25ZsXfEqamgBymP9E5qhEQVFo/edit#gid=0) \n'
        embed=discord.Embed(
            title='BL3 Useful Links',
            description=response,
            color=discord.Color.dark_teal()
        )
        embed.set_footer(text='')
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl3ChatID) and ctx.channel!=officialguild.get_channel(bl3BuildsChatID) and ctx.channel!=officialguild.get_channel(bl3LootChatID):
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(rabidRoleID):
                perms=True
            if perms==True:
                await ctx.send(embed=embed)
            else:
                await ctx.send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.send(embed=embed)


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
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl3ChatID) and ctx.channel!=officialguild.get_channel(bl3BuildsChatID) and ctx.channel!=officialguild.get_channel(bl3LootChatID):
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(rabidRoleID):
                perms=True
            if perms==True:
                await ctx.send(embed=embed)
            else:
                await ctx.send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.channel.send(embed=embed)

    
    @cog_ext.cog_slash(name='bl2info', description='Various Useful Links for BL2')
    async def bl2_info(self, ctx: SlashContext):
        response='[BL2 Basics Guide](https://forums.gearboxsoftware.com/t/guide-borderlands-2-basics-for-new-players/1248201) \n'
        response+='[BL2 UVHM Survival Guide](https://forums.gearboxsoftware.com/t/100-ways-to-stay-alive-in-uvhm/77751) \n'
        response+='[BL2 Splash Damage Guide](https://forums.gearboxsoftware.com/t/complete-splash-damage-guide/1553510) \n'
        response+='[BL2 Critical Hits Guide](https://forums.gearboxsoftware.com/t/guide-critical-hit-bonus-sources-bl2-version/617954) \n'
        response+='[BL2 Parts Guide](https://bl2.parts/) \n'
        response+='[BL2 Save Editor](https://github.com/gibbed/Gibbed.Borderlands2/releases) \n'
        response+='[BL2 Loot Information](https://www.lootlemon.com/) \n'
        response+='[BL2 Tediore Reload Guide](https://forums.gearboxsoftware.com/t/complete-tediore-reload-guide/1591640) \n'
        response+='[BL2 Digistruct Peak Resistances Guide](https://forums.gearboxsoftware.com/t/digistruct-peak-enemy-typing-issue-and-why-your-fire-guns-suck-there/1119745) \n'
        embed=discord.Embed(
            title='BL2 Useful Links',
            description=response,
            color=discord.Color.dark_teal()
        )
        embed.set_footer(text='')
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID):
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(rabidRoleID):
                perms=True
            if perms==True:
                await ctx.send(embed=embed)
            else:
                await ctx.send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.send(embed=embed)


    @cog_ext.cog_slash(name='bl2files', description='Links to the Nexus Mods Page for BLCMM')
    async def database2(self, ctx: SlashContext):
        embed=discord.Embed(
            title='Borderlands Community Mod Manager',
            description='[Nexus Mod Page Link](https://www.nexusmods.com/borderlands2/mods/61)',
            color=discord.Color.dark_green()
        )
        embed.set_footer(text='Courtesy of LightChaosman')
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID):
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(rabidRoleID):
                perms=True
            if perms==True:
                await ctx.send(embed=embed)
            else:
                await ctx.send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.channel.send(embed=embed)

    
    #TODO Turn this into a thing for all the BL2 Character Guides pinned in #borderlands-2
    @cog_ext.cog_slash(name='bl2chars', description='Google Docs of Borderlands 2 Vault Hunter Guides')
    async def bl2_vhguides(self, ctx: SlashContext):
        response=':purple_heart:[Zer0 Guide](https://docs.google.com/document/d/1PEenTeIMyiTyniphG4Kwq7coQz2ZRxJm0HorcXp6ZVU/edit) \n \n'
        response+=':green_heart:[Axton Guide](https://docs.google.com/document/d/1Ogjsyad8chlCQeFnB_KuWkgHqQFVNdTcgWWfijml-4s/edit) \n \n'
        response+=':heart:[Krieg Guide](https://docs.google.com/document/d/1RIIZ5IVaDBtxKdcBdd-SiudTUgTVwuNa88Zi-qVSIOI/edit) \n \n' 
        response+=':brown_heart:[Salvador Guide](https://docs.google.com/document/d/1fK9w9ZmgSvXl-Dq7ICaxA5rBbX4JYlk6KSAldjTIIyU/edit) \n \n' 
        response+=':yellow_heart:[Maya Guide](https://docs.google.com/document/d/17gqutA_GEFFvyV2W-kxoWVLf2TOLmFv9xkfBFVkF3uk/edit)'
        embed=discord.Embed(
            title='BL2 VH Guides',
            description=response,
            color=discord.Color.dark_gold()
        )
        embed.set_footer(text='')
        officialguild=self.bot.get_guild(officialServerID)
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID):
                print('Hey you fucked up')
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(rabidRoleID):
                perms=True
            if perms==True:
                await ctx.send(embed=embed)
            else:
                await ctx.send('Oops! You do not have the proper permissions for that.')
        else:
            await ctx.send(embed=embed)


    #TODO Edit Agonizer rates for various Mayhem Levels
    #TODO Rewrite this method to be a lot cleaner maybe? Maybe don't repeat the link creation but instead create a general one?
    #@commands.command(name='dropinfo', help='Search Command for Finding the Drop Rate and Location of an Item')
    @cog_ext.cog_slash(name='dropinfo', description='Search Command for Finding the Drop Rate and Location of an Item', options=[create_option(name='game', description='Name of Which Game to Search for Drop Rates (BL2/BL3)', option_type=3, required=True),create_option(name='queryname', description='Name of Item to Search For', option_type=3, required=True)])
    async def bl_droprate(self, ctx: SlashContext, game:str, queryname: str):
        officialguild=self.bot.get_guild(officialServerID)
        perms=True
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl3ChatID) and ctx.channel!=officialguild.get_channel(bl3BuildsChatID) and ctx.channel!=officialguild.get_channel(bl3LootChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID):
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if ctx.author.top_role>=officialguild.get_role(rabidRoleID):
                perms=True
            if perms==False:
                await ctx.send('Oops! You do not have the proper permissions for that.')
        if len(queryname)<3:
            await ctx.send('Name \'{}\' too short for searching. Please use at least 3 characters.'.format(queryname))
            return
        if perms==True:
            found=False
            embed=None
            name=''
            itemtype='weapon'
            lootlemon=''
            dir=os.path.dirname(__file__)
            if '3' in game:
                with open(os.path.join(dir, 'utils/droprates3.csv'), newline='') as csvfile:
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
                                title='Drop Info for {} (BL3)'.format(name),
                                description=response,
                                color=discord.Color.purple()
                            )
                            embed.add_field(name='\u200B', value='[Further Information on Lootlemon]({})'.format(lootlemon), inline=True)
                            await ctx.send(embed=embed)
                            if name.lower()=='bearcat':
                                await ctx.send(':pray:')
                            found=True
            if '2' in game:
                with open(os.path.join(dir, 'utils/droprates2.csv'), newline='') as csvfile:
                    lreader=csv.reader(csvfile, delimiter=',', quotechar='|')
                    for row in lreader:
                        response=''
                        queryname=queryname.replace("'","")
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
                            linkname=linkname.replace(' ', '-')
                            linkname=linkname.replace('.','-')
                            lootlemon='https://lootlemon.com/{}/{}-bl2'.format(itemtype, linkname)
                            if 'slayer of' in queryname.lower():
                                lootlemon='https://www.lootlemon.com/search?query=slayer+of+terramorphous'
                            embed=discord.Embed(
                                title='Drop Info for {} (BL2)'.format(name),
                                description=response,
                                color=discord.Color.purple()
                            )
                            embed.add_field(name='\u200B', value='[Further Information on Lootlemon]({})'.format(lootlemon), inline=True)
                            await ctx.send(embed=embed)
                            if name.lower()=='bearcat':
                                await ctx.send(':pray:')
                            found=True
            if found==False:
                await ctx.send('No Item with Name \'{}\' could be found.'.format(queryname))
        

def setup(bot):
    bot.add_cog(Resources(bot))