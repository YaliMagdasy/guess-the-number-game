import random

class NumberGuessingGame:
    def __init__(self, MIN: int=1, MAX: int=100, difficulty: str="normal"):
        self.__validate_and_set(MIN, MAX, difficulty)

    def set_settings(self, MIN: int=None, MAX: int=None, difficulty: str=None):
        new_min = MIN if MIN is not None else self.MIN
        new_max = MAX if MAX is not None else self.MAX
        new_diff = difficulty if difficulty is not None else self.difficulty
        
        self.__validate_and_set(new_min, new_max, new_diff)

    def __validate_and_set(self, MIN, MAX, difficulty):
        if not isinstance(difficulty, str):
            raise ValueError("Difficulty must be a string.")
        
        diff_lower = difficulty.lower()
        if diff_lower not in ["normal", "hard"]:
            raise ValueError("Difficulty must be either 'normal' or 'hard'.")
            
        if MIN >= MAX:
            raise ValueError("Minimum number must be less than the maximum number.")
        
        self.MIN = MIN
        self.MAX = MAX
        self.difficulty = diff_lower

    def get_random_number(self):
        return random.randint(self.MIN, self.MAX)
    
    def start(self):
        random_number = self.get_random_number()

        print(f"\n" + "-"*50)
        print(f"Guess the number from {self.MIN} to {self.MAX}")
        print(f"Difficulty: {self.difficulty.upper()}")
        print("-" * 50)
        
        tries = 0

        while True:
            try:
                user_input = input("\nEnter your guess: ")
                user_number = int(user_input)
            except ValueError:
                print("Please enter a valid whole number.")
                continue

            if user_number < self.MIN or user_number > self.MAX:
                print(f"Are you even trying? {user_number} isn't even between {self.MIN} and {self.MAX}!")
                print("I will give you another chance... :P")
                continue

            tries += 1

            if user_number == random_number:
                print(f"Well done, you got it in {tries} guess{'es' if tries > 1 else ''}!\n")
                
                play_again = ''
                while play_again not in ['y', 'n']:
                    play_again = input("Would you like to play again? (y/n): ").lower()

                if play_again == 'y':
                    random_number = self.get_random_number()
                    tries = 0
                    print(f"\nNew number generated! Range: {self.MIN} to {self.MAX}")
                else:
                    print("\nThanks for playing!\n")
                    break

            elif self.difficulty == "hard" and abs(user_number - random_number) == 1:
                print("SO CLOSE! But on Hard Mode, the number changes when you're off by one!")
                
                new_number = self.get_random_number()
                while new_number == random_number:
                    new_number = self.get_random_number()
                
                random_number = new_number
                print("A new random number has been generated.")
                
            elif user_number < random_number:
                print(f"Your number is SMALLER than the random number.")
            else:
                print(f"Your number is GREATER than the random number.")

if __name__ == "__main__":
    game = NumberGuessingGame(1, 10, "hard")
    game.start()