#this will be modified; just a testing tool right now
import player_setup
import combat_functions
from combat_functions import shot_maker

offense_type = raw_input("What type of shot do you take? (long, mid, close) ")

shot_func = "shot_" + offense_type

print shot_maker(shot_func)

raw_input()

