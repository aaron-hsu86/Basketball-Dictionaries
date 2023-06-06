players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
# Assignment Tasks
# Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    all_players = {}
    def __init__(self, player_data):
        self.name = player_data['name']
        self.age = player_data['age']
        self.position = player_data['position']
        self.team = player_data['team']
    # NINJA BONUS
    @classmethod
    def get_team(cls, team_list):
        new_players = []
        for player in team_list:
            new_players.append(cls(player))
        return new_players

# solution to add list of players to Player class as a dynamic list
for idx in enumerate(players): # enumerate so index values can be taken
    Player.all_players.update({f"player_{players[idx[0]]['name'].split(' ')[0].lower()}" : Player(players[idx[0]])})
    # idx[0] = index value
    # players[index]['name'] grabs player 'name' value
    # .split(' ')[0] splits name into an array of all the strings
    # [0] grabs the first string (in this case, first name)
    # .lower() changes to all lowercase
    # iterating through loop will generate results like {'player_kevin': Player(kevin)} since kevin is the first user

# Challenge 2: Create instances using individual player dictionaries
# Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.
kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Challenge 3: Make a list of Player instances from a list of dictionaries
# Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

# ... (class definition and large list of players here)
new_team = []
new_team2 = {}

# Write your for loop here to populate the new_team variable with Player objects.
for player in players:
    new_team.append(Player(player))

# new_team2 that is a dict instead of a list
# using solution above, instead of pushing into the class, this creates the dict outside and pushes to dict new_team2
for idx in enumerate(players):
    new_team2.update({f"player_{players[idx[0]]['name'].split(' ')[0].lower()}" : Player(players[idx[0]])})

# NINJA BONUS: Add a get_team(cls, team_list) @class method
# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!
new_team3 = Player.get_team(players)
print(new_team3)