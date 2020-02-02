"""
Script to handle Zane related Math calculations
@author Prismatic
"""


experimental_munitions = 0

def skillsSpec(tree, mods, gear):
    import calcMain
    confident_competence = tree[6]
    cold_bore = tree[15]
    violent_momentum = tree[16]
    death_follows_close = tree[20]
    synchronicity = tree[25]
    donnybrook = tree[28]
    trick_of_the_light = tree[37]
    double_barrel = tree[38]

    mods[0] = mods[0] + eval(death_follows_close)
    normal_hit = [confident_competence, violent_momentum, synchronicity, donnybrook, double_barrel]

    normal = zane_normal_hit(normal_hit, mods) + gear[0]
    v1=0 + gear[1]
    v2=0 + gear[2]
    splash= 0 + gear[3]
    elemental = 0 + gear[4]
    critical = 0 + gear[5] 
    bonus_cryo = (0.06 * eval(cold_bore)) + (0.12 * eval(trick_of_the_light)) + gear[6]
    
    mults = [normal, v1, v2, splash, elemental, critical, bonus_cryo]

    response, body, crit = calcMain.BLCalc.calc_Damage(mults)

    bonus_ele, body_1, crit_1 = calcMain.BLCalc.calc_bonus_elements(mults)
    if crit_1 != 0: response = response + "\n" + bonus_ele
    
    body = body + body_1
    crit = crit + crit_1

    response = response + "\n\nCombining Everything:\n**Peak Damage Multiplier:** " + str(round(body, 2)) + "\n**Peak Crit Damage Multiplier:** " + str(round(crit, 2))

    return response


"""
gun skills {confident_competence, violent_momentum, synchronicity, donnybrook, double_barrel}
skill modifiers {death_follows_close, kill_skill_stacks, active_action_skills, movement_speed_over_base}
"""
def zane_normal_hit(gun_skills, skill_modifiers):
    dfc = 1+0.25*float(skill_modifiers[0])
    return (0.35*float(gun_skills[0]))+(0.16*float(gun_skills[1])*skill_modifiers[3]*dfc)+(0.04*float(gun_skills[1])*dfc)+(0.04*float(gun_skills[2])*skill_modifiers[2])+(0.03*float(gun_skills[3])*dfc*skill_modifiers[1])+(0.25*float(gun_skills[4]))