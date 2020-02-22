# calcMain.py
# base code provided by @Prismatic

# Clean up code to catch and explain exceptions/errors
# Implement Official Website Trees


import discord
from discord.ext import commands
from utils import urlDecrypt as url
from utils import mathMoze as Moze
from utils import mathZane as Zane
from utils import mathAmara as Amara
from utils import mathFL4K as FL4K


class BLCalc(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='compare', help='Compare 2 Damage Value Types Against Each Other')
    async def compare(self, ctx, current1, current2, bonus1):
        bonus2=bonus1*(1+current2)/(1+current1)
        response=bonus2
        await ctx.send(response)


    """
    gear {Normal hit, v1, v2, Splash, elemental, crit, bonus element}
    """
    def unpack(link, mods, gear, author="Testing"):
        toReturn=""
        
        if "bl3zone.com" in link:
            index = link.find("planner/")+11
            if "A" == link[index-1]:
                skills = url.zoneAmaraSpec(link[index:len(link)+1])
                toReturn = Amara.skillsSpec(skills, mods, gear)
            elif "B" == link[index-1]:
                skills = url.zoneFlakSpec(link[index:len(link)+1])
                toReturn = FL4K.skillsSpec(skills, mods, gear)
            elif "C" == link[index-1]:
                skills = url.zoneMozeSpec(link[index:len(link)+1])
                toReturn = Moze.skillsSpec(skills, mods, gear)
            elif "D" == link[index-1]:
                skills = url.zoneZaneSpec(link[index:len(link)+1])
                toReturn = Zane.skillsSpec(skills, mods, gear)
        
        elif "bl3skills" in link:
            index = link.find("#")+1
            if "gunner" in link:
                skills = url.skillsMozeSpec(link[index:len(link)+1])
                toReturn = Moze.skillsSpec(skills, mods, gear)
            elif "operative" in link:
                skills = url.skillsZaneSpec(link[index:len(link)+1])
                toReturn = Zane.skillsSpec(skills, mods, gear)
            elif "siren" in link:
                skills = url.skillsAmaraSpec(link[index:len(link)+1])
                toReturn = Amara.skillsSpec(skills, mods, gear)
            elif "beastmaster" in link:
                skills = url.skillsFlakSpec(link[index:len(link)+1])
                toReturn = FL4K.skillsSpec(skills, mods, gear)
        
        print(str(author) + "\n\n" + toReturn)
        return toReturn


    """
    mults {Normal hit, v1, v2, Splash, elemental, crit, bonus element}
    """
    def calc_bonus_elements(mults, experimental_munitions=0):
        bonus_element = mults[6] * (1+mults[0]) * (1+mults[1]) * (1+mults[2]) * (1+mults[4])
        str_bonus_element = "Bonus Element Damage: " + str(round(bonus_element,2))

        crit_bonus_element = (bonus_element+experimental_munitions) * 2 * (1+mults[5])
        str_crit_bonus_element = "Critical Bonus Element Damage: " + str(round(crit_bonus_element,2))
        return str_bonus_element + "\n" + str_crit_bonus_element, bonus_element, crit_bonus_element


    """
    mults is expected to be a list of modifiers
    {Gun Damage, V1, V2, Splash, Elemental, Critical, Bonus Element}
    """
    def calc_Damage(mults):
        damage = (1+mults[0]) * (1+mults[1]) * (1+mults[2]) * (1+mults[3]) * (1+mults[4])
        body = "Damage: " + str(round(damage,2))

        crit_damage = damage * 2 * (1+mults[5])
        crit = "Critical Hit Damage: " + str(round(crit_damage,2))
        return body + "\n" + crit, damage, crit_damage


    @commands.command(name='calc', help='Calculate Your Builds Damage, Use VH Specific Help Commands for Further Info')
    async def bl_calc(self, ctx):
        args=ctx.message.content.split(" ")
        mods=[]
        for i in range(2, 6):
            mods.append(eval(args[i]))
        gear=[]
        for i in range(6, len(args)):
            gear.append(eval(args[i]))
        while len(gear)<7: gear.append(0)
        response=BLCalc.unpack(args[1], mods, gear)
        await ctx.channel.send(response)


    @commands.command(name='calchelp', help='General Format Display for Calc Command')
    async def calchelp(self, ctx):
        response='(Command Template: ~calc bl3skills/bl3zone_link arguments) When entering arguments, just type the number and hit space, do not encase in brackets or separate by commas'
        await ctx.channel.send('```{}```'.format(response))

    
    @commands.command(name='mmozehelp', help='Use for Further VH Calc Info')
    async def mmozehelp(self, ctx):
        response='Arguments: [Click Click (0-1), DiB Stacks, DM (0-1), Phalanx]\n\n These Arguments Are Required. If They Dont Apply, Enter 0.'
        await ctx.channel.send('```{}```'.format(response))

    
    @commands.command(name='mzanehelp', help='Use for Further VH Calc Info')
    async def mzanehelp(self, ctx):
        response='Arguments: [Bonus DFC Points, Kill Skill Stacks, Number of Active Action Skills, Movespeed Bonuses]\n\n These Arguments Are Required. If They Dont Apply, Enter 0.'
        await ctx.channel.send('```{}```'.format(response))

    
    @commands.command(name='mamarahelp', help='Use for Further VH Calc Info')
    async def mamarahelp(self, ctx):
        response='Arguments: [Personal Space Strength (0-1), Samsara Stacks, unused, unused]\n\n These Arguments Are Required. If They Dont Apply, Enter 0.'
        await ctx.channel.send('```{}```'.format(response)) 

    
    @commands.command(name='mfl4khelp', help='Use for Further VH Calc Info')
    async def mfl4khelp(self, ctx):
        response='Arguments: [Big Game Bonus Points, Furious Attack Stacks, Int Stalker Stacks, Full Health or Not (0-1, for Power Inside)]\n\n These Arguments Are Required. If They Dont Apply, Enter 0.'
        await ctx.channel.send('```{}```'.format(response)) 


def setup(bot):
    bot.add_cog(BLCalc(bot))
