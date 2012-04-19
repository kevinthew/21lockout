import csv

rawplayerdata = csv.DictReader(open('testing.csv', 'rb'))

dict_list = []

for line in rawplayerdata:
    dict_list.append(line)


#use this to snag a particular value attached to a particular index with 'Player' as key
#print dict_list[0].get('Player')

dict_length = len(dict_list)
dict_max = dict_length
dict_counter = 0

#return dict_lists' index number for a given player's name; see below
player_key = {}

while dict_counter < dict_max:
    #print dict_counter
    player_key[dict_list[dict_counter].get('Player')] = dict_counter
    dict_counter = dict_counter + 1

player_card = dict_list

print player_card[player_key['LeBron James']].get('Height')






