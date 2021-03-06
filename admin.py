"""
A simple script to help fill the database with data
"""

from app import db, Goal

class Admin(object):
    """
    This class allows for a continuous entry of goals to the database. It basically switches between the home and add_goal
    methods based on the users command. One data is entered correctly, a success message will display. 
    """
    def home(self):
        """
        The main menu
        """
        print("""
DATA ENTRY ADMIN
----------------
Choose an option:
    Add (g)oal
    or (q)uit
""")
        choice = input('Choice: ')

        if choice.lower() == 'g':
            self.add_goal()
                
        elif choice.lower() == 'q':
            print('Goodbye')
        
        else:
            print("{} is not an option!".format(choice.lower))
            self.home()

    def add_goal(self):
        """
        The user fills in the fields using the input function and the transaction with the database is performed automatically 
        """
        goalscorer = input('Who scored? ')
        minute = input('Minute: ')
        method = input('Method ie. header, outside box, inside box, freekick: ')
        round = input('round from 1-4, and quarter, semi and final: ')
        country = input('country that scored: ')
        continent = input('continent the country are from: ')
        phase = input('phase ie counter, set-piece, open-play: ')

        goal = Goal(
            goalscorer,
            minute,
            method,
            round,
            country,
            continent,
            phase
        )

        db.session.add(goal)

        try:
            db.session.commit()
            input('Goal by {} added successfully!'.format(goalscorer))
        except Exception as e:
            print(e)
            input('There appears to have been an error..')

        self.home()
    
    

if __name__ == '__main__':
    Admin().home()