import random
import time

class SlotMachine:
    """Class to simulate a slot machine game with betting and payouts."""
    
    def __init__(self):
        """Initialize the slot machine with game options and state."""
        self.options = ("A", "B", "C", "D", "E", "F", "7")
        self.balance = 0
        self.bet_lines = 0
        self.bet_amount = 0
        self.winning = 0

    def get_user_input(self) -> tuple[int, int, int]:
        """Prompt user for deposit, bet lines, and bet amount with validation.
        
        Returns:
            tuple: Deposit amount, number of bet lines, and bet amount.
        """
        print("---------------------------------")
        while True:
            try:
                deposit = int(input("Enter the amount you want to deposit: $"))
                if deposit <= 0:
                    print("Please enter a positive amount!")
                    time.sleep(1)
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
                time.sleep(1)

        while True:
            try:
                bet_lines = int(input("Enter the number of lines you want to bet on (1, 2, 3): "))
                if bet_lines not in [1, 2, 3]:
                    print("Please enter 1, 2, or 3!")
                    time.sleep(1)
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
                time.sleep(1)

        while True:
            try:
                bet_amount = int(input("Enter the amount you want to bet: $"))
                if bet_amount <= 0 or bet_amount > deposit:
                    print(f"Please enter a positive amount up to ${deposit}!")
                    time.sleep(1)
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
                time.sleep(1)

        self.balance = deposit - bet_amount
        self.bet_lines = bet_lines
        self.bet_amount = bet_amount
        return deposit, bet_lines, bet_amount

    def spin(self) -> tuple[int, int]:
        """Simulate a slot machine spin and calculate winnings.
        
        Returns:
            tuple: Winnings and updated balance.
        """
        print("---------------------------------")
        # Generate 3x3 grid
        line1 = [random.choice(self.options) for _ in range(3)]
        line2 = [random.choice(self.options) for _ in range(3)]
        line3 = [random.choice(self.options) for _ in range(3)]

        # Calculate winnings based on bet lines
        if self.bet_lines == 1:
            line1 = ["X", "X", "X"]
            line3 = ["X", "X", "X"]
            if line2[0] == line2[1] == line2[2] == "7":
                self.winning = self.bet_amount * 7
            elif line2[0] == line2[1] == line2[2]:
                self.winning = self.bet_amount * 5
            elif line2[0] == line2[1] or line2[1] == line2[2] or line2[0] == line2[2]:
                self.winning = self.bet_amount * 4
            else:
                self.winning = 0
        elif self.bet_lines == 2:
            line3 = ["X", "X", "X"]
            if line1[0] == line1[1] == line1[2] == line2[0] == line2[1] == line2[2] == "7":
                self.winning = self.bet_amount * 10
            elif line1[0] == line1[1] == line1[2] == line2[0] == line2[1] == line2[2]:
                self.winning = self.bet_amount * 6
            elif line2[0] == line2[1] == line2[2] == "7" or line1[0] == line1[1] == line1[2] == "7":
                self.winning = self.bet_amount * 5
            elif line2[0] == line2[1] == line2[2] or line1[0] == line1[1] == line1[2]:
                self.winning = self.bet_amount * 2
            else:
                self.winning = 0
        else:  # 3 lines
            if line1[0] == line1[1] == line1[2] == line2[0] == line2[1] == line2[2] == line3[0] == line3[1] == line3[2] == "7":
                self.winning = self.bet_amount * 13
            elif line1[0] == line1[1] == line1[2] == line2[0] == line2[1] == line2[2] == line3[0] == line3[1] == line3[2]:
                self.winning = self.bet_amount * 7
            elif any(line[0] == line[1] == line[2] == "7" for line in [line1, line2, line3]):
                self.winning = self.bet_amount * 3
            elif any(line[0] == line[1] == line[2] for line in [line1, line2, line3]):
                self.winning = self.bet_amount * 1.4
            else:
                self.winning = 0

        # Display the grid
        for row in [line1, line2, line3]:
            print(" | ".join(row))
        
        self.balance += self.winning
        print("---------------------------------")
        print(f"You won: ${self.winning}")
        return self.winning, self.balance

    def play(self) -> None:
        """Run the slot machine game loop with restart option."""
        self.get_user_input()
        self.spin()
        
        while True:
            print("---------------------------------")
            print(f"Your balance: ${self.balance}")
            choice = input("Press 'q' to cash out or 'r' to continue: ").lower()
            if choice == 'q':
                print("Thanks for playing!")
                print(f"You cashed out: ${self.balance}")
                break
            elif choice == 'r':
                if self.balance == 0:
                    print("No money left!")
                    print("Thanks for playing!")
                    break
                self.get_user_input()
                self.spin()
            else:
                print("Please enter 'q' or 'r'!")
                time.sleep(1)

def main():
    """Main function to start the slot machine game."""
    game = SlotMachine()
    game.play()

if __name__ == "__main__":
    main()