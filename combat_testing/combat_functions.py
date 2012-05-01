import random
from data_reader import player_stat_ripper
from player_cards import user_profile, opponent_profile


#feed into probabilities below
offense_name = user_profile['name']
defense_name = opponent_profile['name']
offense_stamina = user_profile['stamina']
defense_stamina = opponent_profile['stamina']
offense_speed = user_profile['speed']
defense_speed = opponent_profile['speed']
defense_mid_stamina = 1.05 * (opponent_profile['stamina']) #these constants are arbitrary; figure out someway to weight this
defense_mid_speed = 1.5 * (opponent_profile['speed'])
defense_close_stamina = 1.5 * (opponent_profile['stamina'])
defense_close_speed = 2 * (opponent_profile['speed'])
offense_mid_stamina = .95 * (user_profile['stamina'])
offense_mid_speed = offense_speed
offense_close_stamina = .75 * (user_profile['stamina'])
offense_close_speed = .75 * (user_profile['speed'])
#how these are defined needs to change; there has to be an easier way

#weighted probabilities
offense_to_take_shot = [float(player_stat_ripper(offense_name, 'TOV%')), (100 - float(player_stat_ripper(offense_name, 'TOV%')))]
defense_to_steal = [(100 - float(player_stat_ripper(defense_name, 'STL%'))), (float(player_stat_ripper(defense_name, 'STL%')))] 
defense_to_block = [(100 - float(player_stat_ripper(defense_name, 'BLK%'))), (float(player_stat_ripper(defense_name, 'BLK%')))]
defense_to_rebound = [(100 - float(player_stat_ripper(defense_name, 'DRB%'))), (float(player_stat_ripper(defense_name, 'DRB%')))]
offense_to_score = '' #see above
offense_to_rebound = [(100 - float(player_stat_ripper(offense_name, 'ORB%'))), (float(player_stat_ripper(offense_name, 'ORB%')))]

#making a defense stat up
def_combined_mod =  100 - (float(player_stat_ripper(defense_name, 'BLK%')) + float(player_stat_ripper(defense_name, 'STL%')))
defense_to_block_and_steal = [def_combined_mod, 100 - def_combined_mod]

#weighted probability roller
def encounterweights(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i
        
#redefine these functions into a class
def stamina_comp_check(ostamina, dstamina):
    if ostamina > dstamina:
        return offense_name
    else:
        return defense_name

def speed_comp_check(ospeed, dspeed):
    if ospeed > dspeed:
        return offense_name
    else:
        return defense_name

######################################
# fail or success checks - merge these functions
######################################

def off_fail_long(fail_check):
    if encounterweights(fail_check) == 0:
        return stamina_comp_check(offense_stamina, defense_stamina)
    else:
        return defense_name

def off_suc_long(suc_check):
    if encounterweights(suc_check) == 0: 
        return offense_name
    else:
        return speed_comp_check(offense_speed, defense_speed) 

def off_fail_mid(fail_check):
    if encounterweights(fail_check) == 0:
        return stamina_comp_check(offense_mid_stamina, defense_mid_stamina)
    else:
        return defense_name

def off_suc_mid(suc_check):
    if encounterweights(suc_check) == 0:
        return offense_name
    else:
        return speed_comp_check(offense_mid_speed, defense_mid_speed)

def off_fail_close(fail_check):
    if encounterweights(fail_check) == 0:
        return stamina_comp_check(offense_close_stamina, defense_close_stamina)
    else:
        return defense_name

def off_suc_close(suc_check):
    if encounterweights(suc_check) == 0:
        return offense_name
    else:
        return speed_comp_check(offense_close_speed, defense_close_speed)


####################################
#long range shot; 3 pt shot
def offense_long_range(offense, defense):
    if encounterweights(offense) == 0: #
        return off_fail_long(defense)
    else:    
        return off_suc_long(defense)
    
#mid range shot; from 10ft to <3 point shot
def offense_mid_range(offense, defense): #
    if encounterweights(offense) == 0: 
        return off_fail_mid(defense)
    else:
        return off_suc_mid(defense) 

#close range shot; from DUNK/layup to 10ft
def offense_close_range(offense, defense):
    if encounterweights(offense) == 0: #
        return off_fail_close(defense)
    else:
        return off_suc_close(defense) 


###############################################
#this needs to be written differently/different spot
#testing output for shot types

def shot_mid():

    i = 0
    counter = []

    while i < 100:

        output_counter = offense_mid_range(offense_to_take_shot, defense_to_block)
        counter.append(output_counter)
        i += 1
    
    counters = ''.join(counter)

    offense_output = offense_name + ' : ' + str(counters.count(offense_name))
    defense_output = defense_name + ' : ' + str(counters.count(defense_name))

    return offense_output + '\n' + defense_output

def shot_long():

    i = 0
    counter = []

    while i < 100:

        output_counter = offense_long_range(offense_to_take_shot, defense_to_steal)
        counter.append(output_counter)
        i += 1
    
    counters = ''.join(counter)

    offense_output = offense_name + ' : ' + str(counters.count(offense_name))
    defense_output = defense_name + ' : ' + str(counters.count(defense_name))

    return offense_output + '\n' + defense_output

def shot_close():

    i = 0
    counter = []

    while i < 100:

        output_counter = offense_close_range(offense_to_take_shot, defense_to_block_and_steal)
        counter.append(output_counter)
        i += 1
    
    counters = ''.join(counter)

    offense_output = offense_name + ' : ' + str(counters.count(offense_name))
    defense_output = defense_name + ' : ' + str(counters.count(defense_name))

    return offense_output + '\n' + defense_output

def shot_maker(shot_value):
    if shot_value == 'shot_close':
        return shot_close()
    if shot_value == 'shot_mid':
        return shot_mid()
    if shot_value == 'shot_long':
        return shot_long()

#I'm sorry world


