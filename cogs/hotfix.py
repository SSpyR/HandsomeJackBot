# hotfix.py
# original code for def bl_hotfix by apocalyptech on GitHub, thanks to him
# see https://github.com/apocalyptech/

# detect additions and removals in hotfix data and state both as such in new hotfix file? (difflib python)
# parsed summary of each changed item ("Changed [Print affected item] [print affected property] to [print new effect]")?
# cant do auto git update with heroku nor point in time, took out for now

# <a:rooHack:652663804840247316> meme emote to add in?

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
        self.sched=AsyncIOScheduler()
        '''self.optinguilds=[]
        self.optinchats=[]
        try:
            with open('utils/optinlistg.pkl', 'rb') as foo:
                self.optinguilds=pkl.load(foo)
            with open('utils/optinlistc.pkl', 'rb') as foo:
                self.optinchats=pkl.load(foo)
        except EOFError:
            print('File Was Empty')'''


    @commands.command(name='hotfix', help='Links to the Commit History Page of the Latest Hotfix to View All Changes')
    async def bl_current_hotfix(self, ctx):
        destchat=None

        for channel in ctx.guild.channels:
            if channel.name=='handsome-jackbot':
                destchat=channel
                await destchat.send('{}'.format(ctx.author.mention))
                await destchat.send('Go To This Link And View The Lastest Commit History To Show Everything Changed With The Latest Hotfix')
                await destchat.send('https://github.com/SSpyR/HandsomeJackBot/commits/master/hotfixes/hotfixes_current.json')
        if destchat==None:
            await ctx.send('handsome-jackbot channel not detected and is required.')


    async def bl_hotfix(self):
        hotfix_url = 'https://discovery.services.gearboxsoftware.com/v2/client/epic/pc/oak/verification'
        output_dir = "/app/hotfixes/"
        point_in_time_base = 'point_in_time'
        point_in_time_dir = os.path.join(output_dir, point_in_time_base)
        cumulative_file = 'hotfixes_current.json'
        new_data = 'new_hotfix.json'

        # Get our cache dir, and create if it doesn't exist
        cache_dir = appdirs.user_cache_dir('hotfixes', 'lavoiet2')
        if not os.path.isdir(cache_dir):
            os.makedirs(cache_dir)
        if not os.path.isdir(cache_dir):
            raise Exception('Couldn\'t create cache dir: {}'.format(cache_dir))

        # Get our current hotfix data, if we can
        hotfix_cache = os.path.join(cache_dir, 'hotfixes.json')
        cur_hotfixes = None
        if os.path.exists(hotfix_cache):
            with open(hotfix_cache) as df:
                cur_hotfixes = df.read()

        # Grab hotfixes (and other data) from server
        r = requests.get(hotfix_url)
        verification = json.loads(r.text)

        # Loop through to find 'Micropatch', which is the one we want
        hotfixes_new = None
        for service in verification['services']:
            if service['service_name'] == 'Micropatch':
                hotfixes_new = service
                break

        # If we didn't get hotfixes, error.
        if not hotfixes_new:
            raise Exception('Could not find hotfixes!')

        # Format them
        hotfixes = json.dumps(hotfixes_new, indent='  ')

        # Check to see if we need to write out a new hotfix file
        do_write = False
        if cur_hotfixes:
            if hotfixes != cur_hotfixes:
                do_write = True
                print('New Hotfix Detected, Preparing Dump')
            else:
                print('No New Hotfix Detected')
                pass
        else:
            do_write = True

        do_write = True
        # Do the write, if we have to
        if do_write:

            # update previous content file
            with open("hotfixes/hotfixes_current.json", "r") as new, open("hotfixes/hotfixes_prev.json", "w") as old:
                old.write(new.read())

            # First write the new file to the cache
            print('Writing new hotfix cache to {}'.format(hotfix_cache))
            with open(hotfix_cache, 'w') as df:
                df.write(hotfixes)

            # Now also write out the hotfixes to a new repo file
            '''now = datetime.datetime.utcnow()
            hotfix_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S.json')
            print('Writing new hotfixes to {}'.format(hotfix_filename))
            with open(os.path.join(point_in_time_dir, hotfix_filename), 'w') as df:
                df.write(hotfixes)'''

            # Now write to our cumulative file
            print('Writing new hotfixes to {}'.format(cumulative_file))
            with open(os.path.join(output_dir, cumulative_file), 'w') as df:
                df.write(hotfixes)

            # Do the git interaction
            print('Pushing to git')
            #repo = git.Repo('/app/')
            remote_repo='https://github.com/SSpyR/HandsomeJackBot.git'
            repo=git.Repo.clone_from(remote_repo, 'heroku')
            repo.git.pull()
            #repo.git.add('--', os.path.join(point_in_time_dir, hotfix_filename))
            repo.git.add('--', os.path.join(output_dir, cumulative_file))
            repo.git.commit('-a', '-m', now.strftime('Auto-update with new hotfixes - %Y-%m-%d %H:%M:%S'))
            repo.git.push("origin", "master")

            # Split the new data out
            startindex=None
            with open('hotfixes/hotfixes_current.json', "r") as f1:
                with open('hotfixes/hotfixes_prev.json', "r") as f2:
                    newdata=json.load(f1)
                    olddata=json.load(f2)
                    for index in reversed(list(enumerate(olddata["parameters"]))):
                        referencepoint=len(olddata["parameters"])-1
                        lastline=olddata["parameters"][referencepoint]
                        for value in newdata["parameters"]:
                            if str(value) in str(lastline):
                                startindex=newdata["parameters"].index(value)
                                break
            with open('hotfixes/hotfixes_current.json', "r") as f1:
                with open('hotfixes/new_hotfix.json', "r") as f2:
                    currentdata=json.load(f1)
                    newdata=json.load(f2)
                    newdata["parameters"].clear()
                    for value in currentdata["parameters"]:
                        if startindex is not None:
                            linevalue=currentdata["parameters"].index(value)
                            if linevalue>startindex:
                                newvalue=currentdata["parameters"][linevalue]
                                newdata["parameters"].append(newvalue)
                        else:
                            print('startindex not assigned')
            with open('hotfixes/new_hotfix.json', "w") as fp:
                json.dump(newdata, fp, indent=4)
            print('New Data Split From Exisiting, Sending..')

            # Send Update to Channels
            '''for glist in range(len(self.optinguilds)):
                for clist in range(len(self.optinchats)):

                    destchat=self.bot.get_guild(self.optinguilds[glist]).get_channel(self.optinchats[clist])
                    print(self.optinguilds[glist])
                    print(self.optinchats[clist])'''
            for guild in self.bot.guilds:
                for channel in guild.channels:

                    destchat=None

                    if channel.name=="handsome-jackbot":
                        destchat=channel
                    else:
                        continue

                    with open('hotfixes/new_hotfix.json') as f:
                        data=json.load(f)

                    await destchat.send('```NEW HOTFIX DATA INCOMING```')
                    await destchat.send('```REMINDER: THIS ONLY DISPLAYS NEW ADDED DATA```')
                    time.sleep(10)

                    for index in enumerate(data['parameters']):
                        response=("```{}```".format(index[1]))
                        if len(response)>=2000:
                            await destchat.send('```Data String too Long, Skipping...```')
                            continue
                        else:
                            await destchat.send(response)
                    await destchat.send('```Data Sent```')
                    await destchat.send('```Use ~hotfix To View More Specific Change History With This Hotfix```')

    
    '''@commands.command(name='test')
    async def test(self, ctx):
        await ctx.send(file=discord.File('/app/hotfixes/hotfixes_current.json'))'''


    def start_sched(self):
        self.sched.start()
        self.sched.add_job(self.bl_hotfix, trigger='interval', minutes=5)
        

def setup(bot):
    Hotfix(bot).start_sched()
    bot.add_cog(Hotfix(bot))
