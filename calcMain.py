# math.py
# base code provided by @Prismatic

# FL4K Math is next
# Clean up code to catch and explain exceptions/errors


import discord
from discord.ext import commands
import mathMoze as Moze
import mathZane as Zane
import mathAmara as Amara


class BLCalc(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot


    '''@commands.command(name='compare', help='Compare 2 Damage Value Types Against Each Other'):
    def compare(self, ctx, current1, current2, bonus1):
        bonus2=bonus1*(1+current2)/(1+current1)
        return bonus2'''


    """
    gear {Normal hit, v1, v2, Splash, elemental, crit, bonus element}
    """
    def unpack(link, mods, gear, author="Testing"):
        if "bl3skills" in link:
            if "gunner" in link:
                toReturn = Moze.skillsSpec(link[link.find("#")+1:len(link)+1], mods, gear)
                print("\n**Moze**")
            elif "operative" in link:
                toReturn = Zane.skillsSpec(link[link.find("#")+1:len(link)+1], mods, gear)
                print("\n**Zane**")
            elif "siren" in link:
                toReturn = Amara.skillsSpec(link[link.find("#")+1:len(link)+1], mods, gear)
                print("\n**Amara**")
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
        response='(Command Template: ~calc bl3skills_link arguments) When entering arguments, just type the number and hit space, do not encase in brackets or separate by commas'
        await ctx.channel.send('```{}```'.format(response))

    
    @commands.command(name='mozehelp', help='Use for Further VH Calc Info')
    async def mozehelp(self, ctx):
        response='Arguments: [Click Click (0-1), DiB Stacks, DM (0-1), Phalanx]\n\n These Arguments Are Required. If They Dont Apply, Enter 0.'
        await ctx.channel.send('```{}```'.format(response))

    
    @commands.command(name='zanehelp', help='Use for Further VH Calc Info')
    async def zanehelp(self, ctx):
        response='Arguments: [Bonus DFC Points, Kill Skill Stacks, Number of Active Action Skills, Movespeed Bonuses]\n\n These Arguments Are Required. If They Dont Apply, Enter 0.'
        await ctx.channel.send('```{}```'.format(response))

    
    @commands.command(name='amarahelp', help='Use for Further VH Calc Info')
    async def amarahelp(self, ctx):
        response='Arguments: [Personal Space Strength (0-1), Samsara Stacks, unused, unused]\n\n These Arguments Are Required. If They Dont Apply, Enter 0.'
        await ctx.channel.send('```{}```'.format(response)) 


def setup(bot):
    bot.add_cog(BLCalc(bot))
