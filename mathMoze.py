"""
Script to handle Moze related Math calculations
@author Prismatic
"""


import math

experimental_munitions = 0

def skillsSpec(tree, mods, gear):
    cloud_of_lead = tree[0]
    stoke_the_embers = tree[3]
    scorching_rpms = tree[7]
    click_click = tree[11]
    fire_in_the_skag_den = tree[13]
    stainless_steel_bear = tree[18]
    short_fuse = tree[25]
    selfless_vengeance = tree[26]
    armored_infantry = tree[28]
    drowning_in_brass = tree[29]
    global experimental_munitions
    experimental_munitions = eval(tree[33])*0.1
    desperate_measures = tree[35]
    phalanx_doctrine = tree[36]
    tenacious_defense = tree[38]

    normal_hit = [click_click, armored_infantry, drowning_in_brass, desperate_measures, phalanx_doctrine, tenacious_defense]
    normal = moze_normal_hit(normal_hit, mods) + gear[0]
    v1=0 + gear[1]
    v2=0 + gear[2]
    splash=0  + gear[3]
    elemental = 0.1 * eval(stoke_the_embers)  + gear[4]
    critical = 0.04 * eval(scorching_rpms)  + gear[5] 
    bonus_fire = (0.0225 * eval(cloud_of_lead)) + (0.03 * eval(selfless_vengeance)) + gear[6]
    skag_den = 0.03 * eval(fire_in_the_skag_den)
    iron_bear_damage = 0.04 * eval(stainless_steel_bear) + 0.05 * eval(scorching_rpms)
    
    mults = [normal, v1, v2, splash, elemental, critical, bonus_fire]

    response, body, crit = math.calc_Damage(mults)

    bonus_ele, body_1, crit_1 = math.calc_bonus_elements(mults, experimental_munitions)
    if crit_1 != 0: response = response + "\n" + bonus_ele

    if skag_den != 0: 
        skag_str, skag_damage = calc_skag_den(mults, skag_den, iron_bear_damage)
        response = response + "\n" + skag_str
        body_1 = body_1 + skag_damage
        crit_1 = crit_1 + skag_damage
    
    body = body + body_1
    crit = crit + crit_1

    if eval(short_fuse) != 0:
        sf_str, body_1, crit_1 = calc_short_fuse(body, crit, mults, iron_bear_damage, skag_den)
        response = response + "\n" + sf_str

    body = body + body_1
    crit = crit + crit_1

    response = response + "\n\nCombining Everything:\n**Peak Damage Multiplier:** " + str(round(body, 2)) + "\n**Peak Crit Damage Multiplier:** " + str(round(crit, 2))

    return response


"""
gun skills {Click Click, Armored Infantry, Drowning in Brass, Desperate Measures, Phalanx Doctrine, Tenacious Defense}
skill modifiers {Click Click, Drowning in Brass, Desperate Measures, Phalanx Doctrine}
"""
def moze_normal_hit(gun_skills, skill_modifiers):
    return (0.12*float(gun_skills[0])*float(skill_modifiers[0]))+(0.03*float(gun_skills[1]))+(0.04*float(gun_skills[2])*float(skill_modifiers[1]))+(0.5/3*float(gun_skills[3])*float(skill_modifiers[2]))+(0.02*float(gun_skills[4])*float(skill_modifiers[3]))+(0.3*float(gun_skills[5]))


def calc_skag_den(mults, skag_den, iron_bear_damage):
    skag_den_damage = skag_den * (1+mults[0]) * iron_bear_damage * (1+mults[4])
    return "Skag Den Bonus Damage: " + str(round(skag_den_damage, 2)), skag_den_damage

def calc_short_fuse(body, crit, mults, iron_bear_damage, skag_den):
    sf_body_damage = body * 0.75 * (1+iron_bear_damage) * (1+mults[3])
    sf_crit_damage = crit * 0.75 * (1+iron_bear_damage) * (1+mults[3])
    sf_body_string = "\nShort Fuse: " + str(round(sf_body_damage,2))
    sf_crit_string = "Short Fuse Critical: " + str(round(sf_crit_damage,2))

    str_skag = ''
    if skag_den != 0:
        skag = body * 0.75 * (1+iron_bear_damage) * skag_den
        body = skag + sf_body_damage
        str_skag = "Short Fuse Skag Den: " + str(round(skag,2))
        skag = crit * 0.75 * (1+iron_bear_damage) * skag_den
        crit = skag + sf_crit_damage
        str_skag = str_skag + "\nShort Fuse Critical Skag Den: " + str(round(skag,2))

    return sf_body_string + "\n" + sf_crit_string + "\n" + str_skag