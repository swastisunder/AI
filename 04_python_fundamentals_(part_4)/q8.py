'''
Create a class Player with:
• a class variable player_count
• instance variables name and level
Track how many players were created.
'''

class Player:
    player_count=0
    
    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count+=1
        
    def get_det(self):
        print(f"Name: {self.name}, Level: {self.level}")
    
    @classmethod
    def display_player_count(cls):
        print(f"Total Player : {cls.player_count}")
        
p1 = Player("Amit", 5)
p1.get_det()
p2 = Player("Rohit", 8)
p2.get_det()
p3 = Player("Sara", 10)
p3.get_det()

Player.display_player_count()