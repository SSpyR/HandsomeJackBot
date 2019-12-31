# datamine.py
# original code for def bl_hotfix by apocalyptech on GitHub, thanks to him
# see https://github.com/apocalyptech/

import os
import sys
import json
import appdirs
import requests
import datetime
import asyncio
import discord

from discord.ext import commands
from apscheduler.schedulers.background import BackgroundScheduler

class Datamine(commands.Cog):

    def __init__(self, bot):
        self.bot=bot
        self.sched=BackgroundScheduler()

    @commands.command
    async def bl_hotfix(self, ctx):
        hotfix_url = 'https://discovery.services.gearboxsoftware.com/v2/client/epic/pc/oak/verification'
        output_dir = "C:\\Users\\lavoiet2\\Downloads\\Coding\\HandsomeJackBot\\hotfixes"
        point_in_time_base = 'point_in_time'
        point_in_time_dir = os.path.join(output_dir, point_in_time_base)
        cumulative_file = 'hotfixes_current.json'

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

        # Do the write, if we have to
        if do_write:

            # First write the new file to the cache
            print('Writing new hotfix cache to {}'.format(hotfix_cache))
            with open(hotfix_cache, 'w') as df:
                df.write(hotfixes)

            # Now also write out the hotfixes to a new repo file
            now = datetime.datetime.utcnow()
            hotfix_filename = now.strftime('hotfixes_%Y_%m_%d_-_%H_%M_%S.json')
            print('Writing new hotfixes to {}'.format(hotfix_filename))
            with open(os.path.join(point_in_time_dir, hotfix_filename), 'w') as df:
                df.write(hotfixes)

            # Now write to our cumulative file
            print('Writing new hotfixes to {}'.format(cumulative_file))
            with open(os.path.join(output_dir, cumulative_file), 'w') as df:
                df.write(hotfixes)

            # Written Extra for Bot, Send Update to Channel
            guild1=self.bot.get_guild(632633098584064018)
            guild2=self.bot.get_guild(639786657666826242)
            chat=self.bot.get_channel(661350189696811094)
            chat2=self.bot.get_channel(661363999656640513)

            '''with open('hotfixes/hotfixes_current.json') as f:
                data=json.load(f)
            with open('hotfixes/hotfixes_current.json', 'w') as f:
                json.dump(data, f)'''

            hotfixes=json.load(hotfixes_new)

            await chat.send('```NEW HOTFIX DATA INCOMING```')
            await chat2.send('```NEW HOTFIX DATA INCOMING```')
            await asyncio.sleep(20)

            for index in enumerate(hotfixes['parameters']):
                response=("```{}```".format(index[1]))
                if len(response)>=2000:
                    await chat.send('```Data String too Long, Skipping...```')
                    await chat2.send('```Data String too Long, Skipping...```')
                    continue
                else:
                    await chat.send(response)
                    await chat2.send(response)
            await ctx.send('```Data Sent```')
                


    @commands.command(name='hotfix', help='Prints out Hotfix Data for Most Recent Hotfix in Designated Chat')
    async def bl_current_hotfix(self, ctx):
        guild1=self.bot.get_guild(632633098584064018)
        guild2=self.bot.get_guild(639786657666826242)
        chat=self.bot.get_channel(661350189696811094)
        chat2=self.bot.get_channel(661363999656640513)
        with open('hotfixes/hotfixes_current.json') as f:
            data=json.load(f)
        with open('hotfixes/hotfixes_current.json', 'w') as f:
            json.dump(data, f)

        await ctx.send('```Preparing Data Dump, See #handsome-jackbot for Results```')
        
        for index in enumerate(data['parameters']):
            response=("```{}```".format(index[1]))
            if ctx.guild==guild1:
                if len(response)>=2000:
                    await chat.send('```Data String too Long, Skipping...```')
                    continue
                else:
                    await chat.send(response)
            if ctx.guild==guild2:
                if len(response)>=2000:
                    await chat2.send('```Data String too Long, Skipping...```')
                    continue
                else:
                    await chat2.send(response)
        await ctx.send('```Data Sent```')
            

    #@bot.command(name='ref')
    #async def bl_ref(self, ctx):

    
    def start_sched(self):
        self.sched.start()
        self.sched.add_job(self.bl_hotfix, trigger='interval', hours=1)
        

def setup(bot):
    Datamine(bot).start_sched()
    bot.add_cog(Datamine(bot))