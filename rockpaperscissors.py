'''

Game : Rock, Paper, Scissors
Created by: Tasawar Ahmed Shuddho

''' 


# MODULES

import random, os


# Declaring constants

ROCK:str = "rock"

PAPER:str = "paper"

SCISSORS:str = "scissors"

MOVES:str = [ROCK, PAPER, SCISSORS]



class PLAYER:

    ''' Player Class. Includes all basic functions to play the game. '''

    # Declaring some global variables for this class only.

    latest_move:str = None 

    def __init__(self) -> None:

        pass

    
    def make_move(self) -> int:

        ''' Requesting Move through terminal input. '''

        PLAYER_INPUT:int = int(input("1. Rock, 2.Paper, 3.Scissors\nEnter Your move(Only enter the number of the move): "))

        self.latest_move = self.__compile_input_to_move(PLAYER_INPUT)


    def __compile_input_to_move(self, player_input:int) -> str:

        ''' Compiler for compiling int to move. '''

        return MOVES[player_input-1]


    def get_current_move(self) -> str:

        ''' Get the latest move by the player through this function. '''

        return self.latest_move
    


class AI_PLAYER(PLAYER):

    ''' Simple AI player. Uses python's core module random. '''

    def make_move(self) -> int:
        
        ''' Making random choice. '''

        AI_INPUT:int =  random.randint(0,2)

        self.latest_move = self.__compile_input_to_move(AI_INPUT)


    def __compile_input_to_move(self, player_input:int) -> str:

        ''' Compiler for compiling int to move. '''

        return MOVES[player_input]


class GAME_IN_TERMINAL:

    ''' Game in terminal. '''

    #Defining variables for this class only.

    player_score = 0

    ai_score = 0 

    def __init__(self) -> None:

        self.player = PLAYER()

        self.ai_player = AI_PLAYER()

        self.__play_game()


    def __play_game(self) -> None:

        ''' Main function of the game. '''

        while True:

            self.player.make_move()

            self.ai_player.make_move()

            os.system("cls")

            print(f"""

            Player Score: {self.player_score}

            AI Score: {self.ai_score}    
            
            """)

            print(f"\n\nPlayer: {self.player.get_current_move()}")

            print(f"AI: {self.ai_player.get_current_move()}")


            ''' Check if the player wins or not. '''

            if self.player.get_current_move() == self.ai_player.get_current_move():

                print("It's a tie!")

            elif self.player.get_current_move() == ROCK:

                if self.ai_player.get_current_move() == PAPER:

                    print("You lose!")

                    self.ai_score += 1

                else:

                    print("You win!")

                    self.player_score += 1

            elif self.player.get_current_move() == PAPER:

                if self.ai_player.get_current_move() == SCISSORS:

                    print("You lose!")

                    self.ai_score += 1

                else:

                    print("You win!")

                    self.player_score += 1

            elif self.player.get_current_move() == SCISSORS:
                    
                    if self.ai_player.get_current_move() == ROCK:
            
                        print("You lose!")

                        self.ai_score += 1

                    else:
                        
                        print("You win!")

                        self.player_score += 1

            print("\n\n")



if __name__ == "__main__":

    GAME_IN_TERMINAL()

