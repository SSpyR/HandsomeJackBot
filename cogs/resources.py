# resources.py

import os
import discord
import json
from discord.colour import Color
import requests
import csv
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_permission
from discord_slash.model import SlashCommandPermissionType
from bot import officialServerID, jackbotChatID, bl3ChatID, bl3BuildsChatID, bl3LootChatID, bl2ChatID, blMediaChatID, invincibleRoleID, ccRoleID, tubbyRoleID, badassRoleID, rabidRoleID

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
			if officialguild.get_role(rabidRoleID) in ctx.author.roles:
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
		response+='[BL3 Save Editor](https://bl3.swiss.dev/proxy) \n'
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
			if officialguild.get_role(rabidRoleID) in ctx.author.roles:
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
			if officialguild.get_role(rabidRoleID) in ctx.author.roles:
				perms=True
			if perms==True:
				await ctx.send(embed=embed)
			else:
				await ctx.send('Oops! You do not have the proper permissions for that.')
		else:
			await ctx.send(embed=embed)


	@cog_ext.cog_slash(name='maurice', description='Information on Where Maurice\'s Black Market is and What its Selling')
	async def bl3_maurice(self, ctx: SlashContext):
		officialguild=self.bot.get_guild(officialServerID)
		location=''
		items=None
		url='https://raw.githubusercontent.com/SSpyR/HandsomeJackBot/master/cogs/utils/blackmarket.json'
		r=requests.get(url)
		bmData=r.json()
		location=bmData['location']
		items=bmData['items']
		item1=items[0]['name']
		item2=items[1]['name']
		item3=items[2]['name']
		shop='{} \n \n'.format(item1)
		shop+='{} \n \n'.format(item2)
		shop+='{} \n \n'.format(item3)
		embed=discord.Embed(
			title='Maurice\'s Black Market',
			description='Due to the change in how Maurice\'s Shop is generated this command will only link to whereismaurice.com until a way is found to dictate the location and store from files each week. Thanks!',
			color=discord.Color.greyple()
		)
		embed.add_field(name='\u200B', value='[Where is Maurice Website](https://whereismaurice.com/)', inline=True)
		if ctx.guild==officialguild:
			if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl3ChatID) and ctx.channel!=officialguild.get_channel(bl3BuildsChatID) and ctx.channel!=officialguild.get_channel(bl3LootChatID):
				return
			perms=False
			#await ctx.send('Request Retrieved')
			if officialguild.get_role(rabidRoleID) in ctx.author.roles:
				perms=True
			if perms==True:
				await ctx.send(embed=embed)
			else:
				await ctx.send('Oops! You do not have the proper permissions for that.')
		else:
			await ctx.send(embed=embed)


	#TODO What do I do about things that by default are listed as no splash damage, but do get anoint?
	#TODO Find all the weapons that get Splash Anoint but dont do splash and add them to the list?
	#TODO Actually fix all the edge cases before releasing again
	#@cog_ext.cog_slash(name='splashinfo', description='Command to see what weapons in Borderlands 3 do Splash and/or get the Splash Anoint', options=[create_option(name='queryname' ,description='Name of Weapon to Search For', option_type=3, required=True)])
	#async def bl3_splashinfo(self, ctx:SlashContext, queryname:str):
	#	officialguild=self.bot.get_guild(officialServerID)
	#	embed=None
	#	perms=True
	#	if ctx.guild==officialguild:
	#		if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl3ChatID) and ctx.channel!=officialguild.get_channel(bl3BuildsChatID) and ctx.channel!=officialguild.get_channel(bl3LootChatID) and ctx.channel!=officialguild.get_channel(blMediaChatID):
	#			return
	#		perms=False
	#		if officialguild.get_role(rabidRoleID) in ctx.author.roles:
	#			perms=True
	#		if perms==False:
	#			await ctx.send('Oops! You do not have the proper permissions for that.')
	#	if len(queryname)<3:
	#		await ctx.send('Name \'{}\' too short for searching. Please use at least 3 characters.'.format(queryname))
	#		return
	#	if perms==True:
	#		found=False
	#		dir=os.path.dirname(__file__)
	#		filepath='utils/splashinfo3.csv'
	#		with open(os.path.join(dir, filepath), newline='') as csvfile:
	#			lreader=csv.reader(csvfile, delimiter=',', quotechar='|')
	#			for row in lreader:
	#				response=''
	#				notes=''
	#				splashemote=':x:'
	#				anointemote=':x:'
	#				if queryname.lower() in row[0].lower():
	#					splashemote=':white_check_mark:'
	#					if len(row[3])>0 and row[3]=='Yes':
	#						splashemote=':x:'
	#					if row[1]=='Yes':
	#						anointemote=':white_check_mark:'
	#					response=f'Does it do Splash: {splashemote}\n\nDoes it get Splash Anoint: {anointemote}'
	#					if len(row[2])>0:
	#						notes=row[2]
	#						response=f'Does it do Splash: {splashemote}\n\nDoes it get Splash Anoint: {anointemote}\n\nNotes: {notes}'
	#					embed=discord.Embed(
	#						title=f'Splash Info for {row[0]}',
	#						description=response,
	#						color=discord.Color.purple()
	#					)
	#					embed.set_footer(text='')
	#					found=True
	#					await ctx.send(embed=embed)
	#		if found==False:
	#			dropsheetpath='utils/droprates3.csv'
	#			with open(os.path.join(dir, dropsheetpath), newline='') as csvfile:
	#				lreader=csv.reader(csvfile, delimiter=',', quotechar='|')
	#				for row in lreader:
	#					if queryname.lower() in row[0].lower():
	#						embed=discord.Embed(
	#							title=f'Splash Info for {row[0]}',
	#							description=f'Does it do Splash: :x:\n\nDoes it get Splash Anoint: :x:',
	#							color=discord.Color.purple()
	#						)
	#						embed.set_footer(text='')
	#						found=True
	#						await ctx.send(embed=embed)
	#		if found==False:
	#			await ctx.send(f'No Item with Name \'{queryname}\' could be found.')


	# @cog_ext.cog_slash(name='bmupdate', description='Command for Spy to Update Black Market', guild_ids=[officialServerID], 
	# options=[create_option(name='location', description='Location of Black Market', option_type=3, required=True),
	# create_option(name='item1', description='Item 1 in Shop', option_type=3, required=True),
	# create_option(name='item2', description='Item 2 in Shop', option_type=3, required=True),
	# create_option(name='item3', description='Item 3 in Shop', option_type=3, required=True)],
	# permissions={officialServerID: [create_permission(98200921950920704, SlashCommandPermissionType.USER, True), create_permission(officialServerID, SlashCommandPermissionType.ROLE, False)]})
	# async def bl3_bmupdate(self, ctx: SlashContext, location:str, item1:str, item2:str, item3:str):
	# 	print('{} {} {} {}'.format(location, item1, item2, item3))
	# 	items=None
	# 	dir=os.path.dirname(__file__)
	# 	json_data={
	# 		'location': location,
	# 		'items': [
	# 			{
	# 				'name': item1
	# 			},
	# 			{
	# 				'name': item2
	# 			},
	# 			{
	# 				'name': item3
	# 			}
	# 		]
	# 	}
	# 	with open(os.path.join(dir, 'utils/blackmarket.json'), 'w') as foo2:
	# 		json.dump(json_data, foo2, indent=4)
	# 	embed=discord.Embed(
	# 		title='Maurice\'s Black Market Update:',
	# 		description='**Location:** {} \n \n **Item 1:** {} \n \n **Item 2:** {} \n \n **Item 3:** {} \n \n'.format(location, item1, item2, item3),
	# 		color=discord.Color.magenta()
	# 	)
	# 	embed.set_footer(text='Information Successfully Updated')
	# 	await ctx.send(embed=embed)

	
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
			if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID) and ctx.channel!=officialguild.get_channel(blMediaChatID):
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
			if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID) and ctx.channel!=officialguild.get_channel(blMediaChatID):
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

	
	#TODO Turn this into a thing for all the BL2 Character Guides pinned in #borderlands-2
	@cog_ext.cog_slash(name='bl2chars', description='Google Docs of Borderlands 2 Vault Hunter Guides')
	async def bl2_vhguides(self, ctx: SlashContext):
		response=':purple_heart:[Zer0 Guide](https://docs.google.com/document/d/1PEenTeIMyiTyniphG4Kwq7coQz2ZRxJm0HorcXp6ZVU/edit) \n \n'
		response+=':green_heart:[Axton Guide](https://docs.google.com/document/d/1Ogjsyad8chlCQeFnB_KuWkgHqQFVNdTcgWWfijml-4s/edit) \n \n'
		response+=':heart:[Krieg Guide](https://docs.google.com/document/d/1RIIZ5IVaDBtxKdcBdd-SiudTUgTVwuNa88Zi-qVSIOI/edit) \n \n' 
		response+=':brown_heart:[Salvador Guide](https://docs.google.com/document/d/1fK9w9ZmgSvXl-Dq7ICaxA5rBbX4JYlk6KSAldjTIIyU/edit) \n \n' 
		response+=':yellow_heart:[Maya Guide](https://docs.google.com/document/d/17gqutA_GEFFvyV2W-kxoWVLf2TOLmFv9xkfBFVkF3uk/edit) \n \n'
		response+=':white_heart:[Gaige Guide](https://docs.google.com/document/d/1wFaN1DLx85cWGEWQwuHkJn-w7hinMy4eUVID0hkt0DI/edit#)'
		embed=discord.Embed(
			title='BL2 VH Guides',
			description=response,
			color=discord.Color.dark_gold()
		)
		embed.set_footer(text='')
		officialguild=self.bot.get_guild(officialServerID)
		if ctx.guild==officialguild:
			if ctx.channel!=officialguild.get_channel(jackbotChatID) and ctx.channel!=officialguild.get_channel(bl2ChatID) and ctx.channel!=officialguild.get_channel(blMediaChatID):
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


def setup(bot):
	bot.add_cog(Resources(bot))
