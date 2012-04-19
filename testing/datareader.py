import csv

#rudimentary sql wannabes
def player_stat_ripper(table_player_name, table_stat_category):

    rawplayerdata = csv.DictReader(open('testing.csv', 'rb'))

    dict_list = []

    for line in rawplayerdata:
        dict_list.append(line)
    
    dict_length = len(dict_list)
    dict_max = dict_length
    dict_counter = 0

    #return dict_lists' index number for a given player's name; see below
    #it's case sensitive; ie Lebron James won't pass but LeBron James does
    player_key = {}

    while dict_counter < dict_max:
        #print dict_counter
        player_key[dict_list[dict_counter].get('Player')] = dict_counter
        dict_counter = dict_counter + 1

    return dict_list[player_key[table_player_name]].get(table_stat_category)


def team_stat_ripper(table_team_name, table_stat_category):

    rawplayerdata = csv.DictReader(open('teamtesting.csv', 'rb'))

    dict_list = []

    for line in rawplayerdata:
        dict_list.append(line)
    
    dict_length = len(dict_list)
    dict_max = dict_length
    dict_counter = 0

    #return dict_lists' index number for a given player's name; see below
    #it's case sensitive; ie Lebron James won't pass but LeBron James does
    team_key = {}

    while dict_counter < dict_max:
        #print dict_counter
        team_key[dict_list[dict_counter].get('team')] = dict_counter
        dict_counter = dict_counter + 1

    return dict_list[team_key[table_team_name]].get(table_stat_category)


#examples
#name = "Jose Barea"
#team = player_stat_ripper(name, 'Team')

#calculates end-to-end speed; calculated by bref position and team pace
def speed_calculator(name):
    playerteam = player_stat_ripper(name, 'Team')
    
    teampace = team_stat_ripper(playerteam, 'adj pace')
    player_base_speed = player_stat_ripper(name, 'Position')
    adj_player_speed = (10 - float(player_base_speed))*10
    player_speed = float(teampace) * (adj_player_speed) * 1.1764705882352941176470588235294 #modifier; Ty Lawson is fastest and '100' with this
    return player_speed

#example
name = 'Ty Lawson'
name1 = 'Nene Hilario'
print name + ' : ' + str(speed_calculator(name))
print name1 + ' : ' + str(speed_calculator(name1))



#build a player_profile class, using all the calculators;
#offense, defense, special offense, special defense, stamina, speed
