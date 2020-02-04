"""
Script to handle Amara related Math calculations

Arguments for mod: [Personal Space Strength, Samsara Stacks, unused, unused]

author @Prismatic
"""

import calcMain

def skillsSpec(tree, mods, gear):

    # Brawl
    personal_space = eval(tree[1])
    arms_deal = eval(tree[3])
    samsara = eval(tree[4])
    jab_cross = eval(tree[11])

    # Mystical Assault
    transcend = eval(tree[18])
    laid_bare = eval(tree[22])
    wrath = eval(tree[23])

    # Fist of the Elements
    tempest = eval(tree[30])
    dread = eval(tree[33])
    forceful_expression = eval(tree[33])

    normal_hit = [samsara, jab_cross, dread, wrath]

    normal = amara_normal_hit(normal_hit, mods) + gear[0]
    v1= (0.25/3*laid_bare) + gear[1]
    v2= (0.177*personal_space*mods[0]) + gear[2]
    splash= (arms_deal * 0.04) + gear[3]
    elemental = (tempest * 0.06) + gear[4]
    critical = (transcend * 0.09) + gear[5] 
    bonus_AS_element = (0.18 * forceful_expression) + gear[6]
    
    mults = [normal, v1, v2, splash, elemental, critical, bonus_AS_element]

    response, body, crit = calcMain.BLCalc.calc_Damage(mults)

    bonus_ele, body_1, crit_1 = calcMain.BLCalc.calc_bonus_elements(mults)
    if crit_1 != 0: response = response + "\n" + bonus_ele
    
    body = body + body_1
    crit = crit + crit_1

    response = response + "\n\nCombining Everything:\n**Peak Damage Multiplier:** " + str(round(body, 2)) + "\n**Peak Crit Damage Multiplier:** " + str(round(crit, 2))

    return response


"""
gun skills {samsara, jab_cross, dread, wrath}
skill modifiers {Personal Space strength, Samsara stacks, unused, unused}
"""
def amara_normal_hit(gun_skills, skill_modifiers):
    return (gun_skills[0]*0.05/3*skill_modifiers[1])+(gun_skills[1]*0.03)+(gun_skills[2]*0.15)+(gun_skills[3]*0.4/3)