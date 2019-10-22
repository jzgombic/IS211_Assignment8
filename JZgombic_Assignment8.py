#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import sys
import time


random.seed(0)


def main():

    number_of_players = int(input("\nPlease enter the number of players: "))

    if (number_of_players<2):
            print ("\nThis is not a one player game, please invite some friends!")
            main()
    else:
        try:
            number_of_players

        except ValueError:
            print ("Kindly input an integer.")
            main()

    try:
        computer_players = int(input("\nHow many of these are Computer players: "))

    except ValueError:
        print ("\nKindly input an integer.")
        main()

    timed()

    human_players = number_of_players - computer_players

    playing = PlayerFactory()

    for num in range(human_players):
        playing.playerNum.append('human')

    for num in range(computer_players):
        playing.playerNum.append('computer')

    playing.getPlayers()
    players = playing.export_list

    TimedGameProxy(players)


class Player(object):

    def __init__(self, playerX):
        self.playerID = playerX
        self.roll = True
        self.total_score = 0
        self.type = 'human'

    def choice(self):

        try:
            choice = input("\nWhat would you like to do: Hold (h) or Roll (r)?")
            
            if choice not in ('h', 'r'):
                raise ValueError

            if choice.lower() == 'h':
                self.roll = False
                print ("\nYour have chosen to Hold. This ends your turn.\n")

            if choice.lower() == 'r':
                self.roll = True
                print ("Rolling.....\n")
                            
        except ValueError:
            print ("\nPlease enter a valid selection: h for Hold or r for Roll.\n")
            self.choice()


class ComputerPlayer(Player):

    def __init__(self, playerX):
        Player.__init__(self, playerX)
        self.type = 'computer'

    def Choice(self, choice):
        if choice.lower() == 'h':
            self.roll = False
            print ("\nThe Computer has chosen to Hold. This ends their turn.\n")

        if choice.lower() == 'r':
            self.roll = True
            print ("Rolling.....\n")


class HumanPlayer(Player):
    pass


class Dice(object):

    def __init__(self):
        self.roll_value = None

    def roll(self):
        self.roll_value = random.randint(1, 6)
        return self.roll_value


class Game(object):

    def __init__(self, playerNum):
        pass

    def change_turn(self, player):
        pass

    def start_turn(self, player):
        pass

class TimedGameProxy(Game):

    def __init__(self, playerNum):

        self.timed = True
        self.starting_time = time.time()
        self.time_limit = timed
        Game.__init__(self, playerNum)
        
        self.players = playerNum
        self.goal = 100

        self.first_player = random.randint(1, (len(self.players) - 1))
        self.next_player = None
        self.dice = Dice()

        self.current_player = self.players[self.first_player]
        print ("\nPlayer {} will go first\n".format(self.current_player.playerID))

        self.start_turn(self.current_player)

    def start_turn(self, player):

        turn_score = 0
        count = len(self.players) - 1
        print ("     The updated scores are as follows:")
        while count >= 0:
            print ("          Player {} has {} points.".format(self.players[count].playerID, self.players[count].total_score))
            count -= 1

        print ("\n\n     Player {}:".format(player.playerID))

        if player.type == 'human':
            player.roll = True
        
            while player.roll:

                die_num = self.dice.roll()

                if die_num == 1:
                    print ("\n          You rolled a 1, your turn score is 0 and the next player will now roll.\n")
                    player.roll = False

                elif (turn_score + player.total_score) >= self.goal:
                    player.roll = False

                elif timer == True and (self.time_limit - (time.time() - self.starting_time) <= 0):
                    player.roll = False
                    
                elif timer == True and (self.time_limit - (time.time() - self.starting_time) > 0):
                    turn_score = turn_score + die_num
                    print ("\nYou now have {:0.2f} seconds left until the game ends.".format(self.time_limit - (time.time() - self.starting_time)))
                    print ("\n          You rolled a {} ".format(self.dice.roll_value))
                    print ("          Your score for this round is {}".format(turn_score))
                    print ("          Your total score for the game is {}".format(player.total_score))
                    print ("          If you decide to hold, your total score will be {}".format((turn_score + player.total_score)))
                    player.choice()

                else:
                    turn_score = turn_score + die_num
                    print ("\n          You rolled a {} ".format(self.dice.roll_value))
                    print ("          Your score for this round is {}".format(turn_score))
                    print ("          Your total score for the game is {}".format(player.total_score))
                    print ("          If you decide to hold, your total score will be {}".format((turn_score + player.total_score)))
                    player.choice()
                
            player.total_score += turn_score
            print ("          Your total score is now {}.\n".format(player.total_score))
            self.change_turn(player)
                    
        if player.type == 'computer':
            player.roll = True

            if 25 < (100 - (turn_score + player.total_score)):
                hold = 25

            elif (100 - (turn_score + player.total_score)) < 25:
                hold = (100 - (turn_score + player.total_score))

            while player.roll:

                die_num = self.dice.roll()

                if die_num == 1:
                    print ("\n          You rolled a 1, your turn score is 0 and the next player will now roll.\n")
                    player.roll = False

                elif (turn_score + player.total_score) >= self.goal:
                    player.roll = False
 
                elif (turn_score + player.total_score) == hold:
                    player.roll = False
 
                elif timer == True and (self.time_limit - (time.time() - self.starting_time) <= 0):
                    player.roll = False

                elif timer == True and (self.time_limit - (time.time() - self.starting_time) > 0):
                    turn_score = turn_score + die_num
                    print ("\nYou now have {:0.2f} seconds left until the game ends.".format(self.time_limit - (time.time() - self.starting_time)))
                    print ("\n          You rolled a {} ".format(self.dice.roll_value))
                    print ("          Your score for this round is {}".format(turn_score))
                    print ("          Your total score for the game is {}".format(player.total_score))
                    
                else:
                    turn_score = turn_score + die_num
                    print ("\n          You rolled a {} ".format(self.dice.roll_value))
                    print ("          Your score for this round is {}".format(turn_score))
                    print ("          Your total score for the game is {}".format(player.total_score))
                    
            player.total_score += turn_score
            print ("          Your total score is now {}.\n".format(player.total_score))
            self.change_turn(player)

    def change_turn(self, player):

        if player.total_score >= self.goal:
            print ("\n          Player {} has won!!!!!!!!".format(player.playerID))
            print ("          Player {} has won!!!!!!!!".format(player.playerID))
            print ("          Player {} has won!!!!!!!!".format(player.playerID))
            self.proceed = False

            try:
                play = input("\n\nWould you like to play again: y for Yes or n for No  ")

                if play.lower() not in ('y', 'n'):
                    raise ValueError

                if play.lower() == 'y':
                    number_of_players = ""
                    computer_players = ""
                    main()

                if play.lower() == 'n':
                    sys.exit

            except ValueError:
                print ("Please enter a valid selection: either y for Yes or n for No.")
                self.replay()

        elif timer == True and (self.time_limit - (time.time() - self.starting_time) <= 0):
            print ("          Time has expired.\n")
            print ("          The final scores are as follows:")
            count = len(self.players) - 1
            while count >= 0:
                print ("               Player {} has {} points.".format(self.players[count].playerID, self.players[count].total_score))
                count -= 1
            self.proceed = False

            try:
                play = input("\n\nWould you like to play again: y for Yes or n for No  ")

                if play.lower() not in ('y', 'n'):
                    raise ValueError

                if play.lower() == 'y':
                    number_of_players = ""
                    computer_players = ""
                    main()

                if play.lower() == 'n':
                    sys.exit

            except ValueError:
                print ("Please enter a valid selection: either y for Yes or n for No.")
                self.replay()

        else:
            if player.playerID == len(self.players):
                self.first_player = 0
                self.current_player = self.players[0]
                self.start_turn(self.current_player)
            else:
                self.first_player += 1
                self.current_player = self.players[self.first_player]
                self.start_turn(self.current_player)
        
        
def timed():
    global timer
    global timed
    timer = False

    try:
        time = input("\n\nWould you like this game to be timed: y for Yes or n for No  ")

        if time.lower() not in ('y', 'n'):
            raise ValueError

        if time.lower() == 'y':
            timer = True

            try:
                timed = int(input("\nPlease enter a time limit (Enter 0 to accept the default of 60 seconds): "))

                if timed == 0:
                    timed = 60
                elif (timed < 0):
                    raise ValueError
                else:
                    timed

            except ValueError:
                print ("Kindly input an integer.")
                timed()
            
            return timer

        if time.lower() == 'n':
            timer = False
            return timer

    except ValueError:
        print ("Please enter a valid selection: either y for Yes or n for No.")
        timer()


class PlayerFactory(object):

    def __init__(self):
        self.playerNum = []
        self.export_list = []

    def getPlayers(self):
        count = 1
        
        for item in self.playerNum:
            if item == 'human':
                self.export_list.append(HumanPlayer(count))
                count += 1
            if item == 'computer':
                self.export_list.append(ComputerPlayer(count))
                count += 1
      

if __name__ == '__main__':
    main()
