# hotfix.py
# original code for def bl_hotfix by apocalyptech on GitHub, thanks to him
# see https://github.com/apocalyptech/

# Just Gonna Embed and Send Out the Auto Update Link From Webhook
# Ctrl+C+K to Mass Comment, Ctrl+K+U to Mass UnComment

import os
import sys
import json
import appdirs
import requests
import datetime
import time
import asyncio
import git
import pickle as pkl
import discord

from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class Hotfix(commands.Cog):

    def __init__(self, bot):
        self.bot=bot
        #self.sched=AsyncIOScheduler()
        #self.optinguilds=[]
        #self.optinchats=[]
        #try:
        #    with open('utils/optinlistg.pkl', 'rb') as foo:
        #        self.optinguilds=pkl.load(foo)
        #    with open('utils/optinlistc.pkl', 'rb') as foo:
        #        self.optinchats=pkl.load(foo)
        #except EOFError:
        #    print('File Was Empty')

    
    @commands.command(name='hotfix', help='Links to the History View of the Latest Hotfix to View All Changes')
    async def bl_hotfix(self, ctx):
        guild=self.bot.get_guild(632633098584064018)
        chat=guild.get_channel(661350189696811094)
        found=False
        async for msg in chat.history(limit=500):
            if msg.author.display_name=='GitHub' and found is False:
                update=msg.embeds[0].to_dict()
                link=update["url"]
                if 'Auto-update' in update["description"]:
                    embed=discord.Embed(
                        title='BL3 Hotfix Auto-Update',
                        description='Latest Updated JSON of BL3 Hotfix Changes',
                        colour=discord.Color.blue()
                    )
                    embed.set_footer(text='Repository Provided by apocaplyptech')
                    embed.set_image(url='https://cdn.2kgames.com/borderlands/news/Article+Embeds/PAXE20/steam-art_560.jpg')
                    embed.set_author(name='HandsomeJackbot', icon_url='https://cdn.2kgames.com/borderlands/news/Article+Embeds/PAXE20/steam-art_560.jpg')
                    embed.add_field(name='Link to Changes', value=link, inline=True)
                    await ctx.send(embed=embed)
                    found=True



    @commands.Cog.listener()
    async def on_message(self, message):
        guild=self.bot.get_guild(632633098584064018)

        if message.guild==guild:
            if message.author.display_name=='GitHub':
                update=message.embeds[0].to_dict()
                link=update["url"]
                if 'Auto-update' in update["description"]:
                    embed=discord.Embed(
                        title='BL3 Hotfix Auto-Update',
                        description='Latest Updated JSON of BL3 Hotfix Changes',
                        colour=discord.Color.blue()
                    )
                    embed.set_footer(text='Repository Provided by apocaplyptech')
                    embed.set_image(url='https://cdn.2kgames.com/borderlands/news/Article+Embeds/PAXE20/steam-art_560.jpg')
                    embed.set_author(name='HandsomeJackbot', icon_url='https://cdn.2kgames.com/borderlands/news/Article+Embeds/PAXE20/steam-art_560.jpg')
                    embed.add_field(name='Link to Changes', value=link, inline=True)
                    for guild in self.bot.guilds:
                        for channel in guild.channels:

                            destchat=None

                            if channel.name=="handsome-jackbot":
                                destchat=channel
                            else:
                                continue

                            await destchat.send(embed=embed)






    #@commands.command(name='hotfix', help='Links to the Commit History Page of the Latest Hotfix to View All Changes')
    #async def bl_current_hotfix(self, ctx):
    #    destchat=None

    #    for channel in ctx.guild.channels:
    #        if channel.name=='handsome-jackbot':
    #            destchat=channel
    #            await destchat.send('{}'.format(ctx.author.mention))
    #            await destchat.send('Go To This Link And View The Lastest Commit History To Show Everything Changed With The Latest Hotfix')
    #            await destchat.send('https://github.com/SSpyR/HandsomeJackBot/commits/master/hotfixes/hotfixes_current.json')
    #    if destchat==None:
    #        await ctx.send('handsome-jackbot channel not detected and is required.')

    
    #@commands.command(name='newhfixfile', help='Sends the New Hotfix File to View New Data in Editors')
    #async def bl_new_hotfix_file(self, ctx):
    #    destchat=None

    #    for channel in ctx.guild.channels:
    #        if channel.name=='handsome-jackbot':
    #            destchat=channel
    #            dir=os.path.dirname(__file__)
    #            await destchat.send('{}'.format(ctx.author.mention))
    #            await destchat.send('Here is the New Hotfix File (This File Contains What JackBot Sends Out in Updates, Just Optional to View as a File)')
    #            await destchat.send(file=discord.File(os.path.join(dir,'hotfixes\\new_hotfix.json')))
    #    if destchat==None:
    #        await ctx.send('handsome-jackbot channel not detected and is required.')


    #@commands.command(name='curhfixfile', help='Sends the Current Hotfix File to View New Data in Editors')
    #async def bl_cur_hotfix_file(self, ctx):
    #    destchat=None

    #    for channel in ctx.guild.channels:
    #        if channel.name=='handsome-jackbot':
    #            destchat=channel
    #            dir.os.path.dirname(__file__)
    #            await destchat.send('{}'.format(ctx.author.mention))
    #            await destchat.send('Here is the Current Hotfix File (This File Contains All Hotfixes that are Active as of Current, Just Optional to View as a File)')
    #            await destchat.send(file=discord.File(os.path.join(dir,'hotfixes\\hotfixes_current.json')))
    #    if destchat==None:
    #        await ctx.send('handsome-jackbot channel not detected and is required.')


    #async def bl_hotfix(self):
    #    dir=os.path.dirname(__file__)
    #    hotfix_url = 'https://discovery.services.gearboxsoftware.com/v2/client/epic/pc/oak/verification'
    #    output_dir = "hotfixes"
    #    point_in_time_base = 'point_in_time'
    #    point_in_time_dir = os.path.join(output_dir, point_in_time_base)
    #    cumulative_file = 'hotfixes_current.json'
    #    new_data = 'new_hotfix.json'

    #    # Get our cache dir, and create if it doesn't exist
    #    cache_dir = appdirs.user_cache_dir('hotfixes', 'lavoiet2')
    #    if not os.path.isdir(cache_dir):
    #        os.makedirs(cache_dir)
    #    if not os.path.isdir(cache_dir):
    #        raise Exception('Couldn\'t create cache dir: {}'.format(cache_dir))

    #    # Get our current hotfix data, if we can
    #    hotfix_cache = os.path.join(cache_dir, 'hotfixes.json')
    #    cur_hotfixes = None
    #    if os.path.exists(hotfix_cache):
    #        with open(hotfix_cache) as df:
    #            cur_hotfixes = df.read()

    #    # Grab hotfixes (and other data) from server
    #    r = requests.get(hotfix_url)
    #    verification = json.loads(r.text)

    #    # Loop through to find 'Micropatch', which is the one we want
    #    hotfixes_new = None
    #    for service in verification['services']:
    #        if service['service_name'] == 'Micropatch':
    #            hotfixes_new = service
    #            break

    #    # If we didn't get hotfixes, error.
    #    if not hotfixes_new:
    #        raise Exception('Could not find hotfixes!')

    #    # Format them
    #    hotfixes = json.dumps(hotfixes_new, indent='  ')

    #    # Check to see if we need to write out a new hotfix file
    #    do_write = False
    #    if cur_hotfixes:
    #        if hotfixes != cur_hotfixes:
    #            do_write = True
    #            print('New Hotfix Detected, Preparing Dump')
    #        else:
    #            print('No New Hotfix Detected')
    #            pass
    #    else:
    #        do_write = True

    #    # Do the write, if we have to
    #    if do_write:

    #        # update previous content file
    #        with open(os.path.join(dir, "hotfixes/hotfixes_current.json"), "r") as new, open(os.path.join(dir, "hotfixes/hotfixes_prev.json"), "w") as old:
    #            old.write(new.read())

    #        # First write the new file to the cache
    #        print('Writing new hotfix cache to {}'.format(hotfix_cache))
    #        with open(hotfix_cache, 'w') as df:
    #            df.write(hotfixes)

    #        # Now also write out the hotfixes to a new repo file
    #        now = datetime.datetime.utcnow()
    #        hotfix_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S.json')
    #        print('Writing new hotfixes to {}'.format(hotfix_filename))
    #        with open(os.path.join(point_in_time_dir, hotfix_filename), 'w') as df:
    #            df.write(hotfixes)

    #        # Now write to our cumulative file
    #        print('Writing new hotfixes to {}'.format(cumulative_file))
    #        with open(os.path.join(output_dir, cumulative_file), 'w') as df:
    #            df.write(hotfixes)

    #        # Do the git interaction
    #        #print('Pushing to git')
    #        #repo = git.Repo("C:\\Users\\lavoiet2\\Downloads\\Coding\\HandsomeJackBot")
    #        #repo.git.pull()
    #        #repo.git.add('--', os.path.join(point_in_time_dir, hotfix_filename))
    #        #repo.git.add('--', os.path.join(output_dir, cumulative_file))
    #        #repo.git.commit('-a', '-m', now.strftime('Auto-update with new hotfixes - %Y-%m-%d %H:%M:%S'))
    #        #repo.git.push("origin", "master")

    #        # Split the new data out
    #        startindex=None
    #        with open(os.path.join(dir, 'hotfixes/hotfixes_current.json'), "r") as f1:
    #            with open(os.path.join(dir, 'hotfixes/hotfixes_prev.json'), "r") as f2:
    #                newdata=json.load(f1)
    #                olddata=json.load(f2)
    #                for index in reversed(list(enumerate(olddata["parameters"]))):
    #                    referencepoint=len(olddata["parameters"])-1
    #                    lastline=olddata["parameters"][referencepoint]
    #                    for value in newdata["parameters"]:
    #                        if str(value) in str(lastline):
    #                            startindex=newdata["parameters"].index(value)
    #                            break
    #        with open(os.path.join(dir, 'hotfixes/hotfixes_current.json'), "r") as f1:
    #            with open(os.path.join(dir, 'hotfixes/new_hotfix.json'), "r") as f2:
    #                currentdata=json.load(f1)
    #                newdata=json.load(f2)
    #                newdata["parameters"].clear()
    #                for value in currentdata["parameters"]:
    #                    if startindex is not None:
    #                        linevalue=currentdata["parameters"].index(value)
    #                        if linevalue>startindex:
    #                            newvalue=currentdata["parameters"][linevalue]
    #                            newdata["parameters"].append(newvalue)
    #                    else:
    #                        print('startindex not assigned')
    #        with open(os.path.join(dir, 'hotfixes/new_hotfix.json'), "w") as fp:
    #            json.dump(newdata, fp, indent=4)
    #        print('New Data Split From Exisiting, Sending..')

    #        # Send Update to Channels
    #        '''for glist in range(len(self.optinguilds)):
    #            for clist in range(len(self.optinchats)):

    #                destchat=self.bot.get_guild(self.optinguilds[glist]).get_channel(self.optinchats[clist])
    #                print(self.optinguilds[glist])
    #                print(self.optinchats[clist])'''
    #        for guild in self.bot.guilds:
    #            for channel in guild.channels:

    #                destchat=None

    #                if channel.name=="handsome-jackbot":
    #                    destchat=channel
    #                else:
    #                    continue

    #                with open(os.path.join(dir, 'hotfixes/new_hotfix.json')) as f:
    #                    data=json.load(f)

    #                await destchat.send('```NEW HOTFIX DATA INCOMING```')
    #                await destchat.send('```REMINDER: THIS ONLY DISPLAYS NEW ADDED DATA```')
    #                time.sleep(10)

    #                for index in enumerate(data['parameters']):
    #                    response=("```{}```".format(index[1]))
    #                    if len(response)>=2000:
    #                        await destchat.send('```Data String too Long, Skipping...```')
    #                        continue
    #                    else:
    #                        await destchat.send(response)
    #                await destchat.send('```Data Sent```')
    #                await destchat.send('```Use ~hotfix To View More Specific Change History With This Hotfix```')


    #def start_sched(self):
    #    self.sched.start()
    #    self.sched.add_job(self.bl_hotfix, trigger='interval', minutes=30)
        

def setup(bot):
    #Hotfix(bot).start_sched()
    bot.add_cog(Hotfix(bot))
