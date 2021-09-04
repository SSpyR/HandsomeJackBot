# dropinfo.py

import os
import csv
import discord
from discord import file
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from bot import officialServerID, jackbotChatID, bl3ChatID, bl3BuildsChatID, bl3LootChatID, bl2ChatID, invincibleRoleID, ccRoleID, tubbyRoleID, badassRoleID, rabidRoleID

class DropInfo(commands.Cog):

    def __init__(self, bot):
        self.bot=bot


    @cog_ext.cog_slash(name='dropinfo', description='Search Command for Finding the Drop Rate and Location of an Item', options=[create_option(name='game', description='Name of Which Game to Search for Drop Rates (BL2/BL3)', option_type=3, required=True),create_option(name='queryname', description='Name of Item or Drop Source to Search For', option_type=3, required=True)])
    async def bl_droprate(self, ctx: SlashContext, game:str, queryname: str):
        officialguild=self.bot.get_guild(officialServerID)
        embed=None
        perms=True
        if ctx.guild==officialguild:
            if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl3ChatID) and ctx.channel!=officialguild.get_channel(bl3BuildsChatID) and ctx.channel!=officialguild.get_channel(bl3LootChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID):
                return
            perms=False
            #await ctx.send('Request Retrieved')
            if officialguild.get_role(rabidRoleID) in ctx.author.roles:
                perms=True
            if perms==False:
                await ctx.send('Oops! You do not have the proper permissions for that.')
        if len(queryname)<3:
            await ctx.send('Name \'{}\' too short for searching. Please use at least 3 characters.'.format(queryname))
            return
        if perms==True:
            found=False
            gameNum=None
            if '3' in game:
                gameNum='3'
            if '2' in game:
                gameNum='2'
            name=''
            itemtype='weapon'
            lootlemon=''
            dir=os.path.dirname(__file__)
            filepath='utils/droprates{}.csv'.format(gameNum)
            with open(os.path.join(dir, filepath), newline='') as csvfile:
                lreader=csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in lreader:
                    response=''
                    queryname=queryname.replace("'","")
                    if 'pat' in queryname.lower():
                        queryname='p.a.t'
                    if queryname.lower() in row[0].lower() or queryname.lower() in row[2].lower():
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
                        lootlemon='https://lootlemon.com/{}/{}-bl{}'.format(itemtype, linkname, gameNum)
                        if 'slayer of' in queryname.lower():
                            lootlemon='https://www.lootlemon.com/search?query=slayer+of+terramorphous'
                        embed=discord.Embed(
                            title='Drop Info for {} (BL{})'.format(name, gameNum),
                            description=response,
                            color=discord.Color.purple()
                        )
                        embed.add_field(name='\u200B', value='[Further Information on Lootlemon]({})'.format(lootlemon), inline=True)
                        found=True
                        await ctx.send(embed=embed)
                        if name.lower()=='bearcat':
                            await ctx.send(':pray:')
            if found==False:
                await ctx.send('No Item or Source with Name \'{}\' could be found.'.format(queryname))


def setup(bot):
    bot.add_cog(DropInfo(bot))