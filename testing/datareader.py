import csv


def table_ripper(table_name, table_stat):

    rawplayerdata = csv.DictReader(open('testing.csv', 'rb'))

    dict_list = []

    for line in rawplayerdata:
        dict_list.append(line)
    
    dict_length = len(dict_list)
    dict_max = dict_length
    dict_counter = 0

    #return dict_lists' index number for a given player's name; see below
    #it's CASE SENSITIVE RIGHT NOW; ie Lebron James doesn't work but LeBron James does
    player_key = {}

    while dict_counter < dict_max:
        #print dict_counter
        player_key[dict_list[dict_counter].get('Player')] = dict_counter
        dict_counter = dict_counter + 1

    player_card = dict_list

    return player_card[player_key[table_name]].get(table_stat)


#example
print table_ripper('LeBron James', 'Height')

