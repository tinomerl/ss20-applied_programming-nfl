# choose a specific NFL division (4 teams) from table at https://en.wikipedia.org/wiki/National_Football_League#Teams
# create dictionary of following structure for chosen division
division = {
    "team_id1": {
        "name": "Bufallo Bills",
        "city": "Orchard Park, New York",
        "est": 1960,
        "coach": "Sean McDermott",
    },
    "team_id2": {
        "name": "Miami Dolphins",
        "city": "Miami Gardens, Florida",
        "est": 1966,
        "coach": "Brian Flores",
    },
    "team_id3": {
        "name": "New England Patriots",
        "city": "Foxborough, Massachusetts",
        "est": 1960,
        "coach": "Bill Belichick",
    },
    "team_id4":{
        "name": "New York Jets",
        "city": "East Rutherford, New Jersey",
        "est": 1960,
        "coach": "Adam Gase",
    },
}
def getFoundingYear(name):
    # add code for getting founding year of team identified by full team name
    # should return an integer value (relevant for getOlder() method)
    
    #For Loop to iterate over division dictionary
    for items in division.items():
        #if we have a match to name return established year
        if items[1]['name'] == name:
            return items[1]['est']
          

def getOlderTeam():
    # add code for returning string which explains which team is older 
    pass



