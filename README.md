# Slot Machine Simulator

A Python-based command-line slot machine game where players can deposit money, choose bet lines, place bets, and spin to win based on symbol combinations.

## Features





Interactive Gameplay: Deposit funds, select 1-3 bet lines, and set bet amounts.



Randomized Spins: Simulates a 3x3 slot machine grid with symbols (A, B, C, D, E, F, 7).



Dynamic Payouts: Winnings vary based on bet lines and symbol matches (e.g., triple "7" or matching symbols).



Balance Management: Tracks player balance, updates after each spin, and allows cashing out.



Input Validation: Ensures valid user inputs for deposits, bet lines, and bet amounts.

## Requirements





Python 3.x



Standard libraries: random, time

## How to Run





Clone or download the repository.



Navigate to the project directory.



## Run the script:

python slot_machine.py



Follow the prompts to:





Deposit an amount.



Choose 1, 2, or 3 bet lines.



Set a bet amount.



Spin and view results.



Press r to continue or q to cash out.

## Gameplay





Symbols: A, B, C, D, E, F, 7



Bet Lines:





1 line: Middle row only.



2 lines: Top and middle rows.



3 lines: All rows.



Payouts (multipliers applied to bet amount):





1 Line:





Triple "7": 7x



Triple same symbol: 5x



Two matching symbols: 4x



2 Lines:





Both rows triple "7": 10x



Both rows same symbol: 6x



One row triple "7": 5x



One row same symbol: 2x



3 Lines:





All rows triple "7": 13x



All rows same symbol: 7x



Any row triple "7": 3x



Any row same symbol: 1.4x



The game displays the 3x3 grid after each spin, shows winnings, and updates the balance.

File Structure





slot_machine.py: Main script containing the SlotMachine class and game logic.

## Example


Enter the amount you want to deposit: $100
Enter the number of lines you want to bet on (1, 2, 3): 2
Enter the amount you want to bet: $20

A | B | C
7 | 7 | 7
X | X | X

You won: $100

Your balance: $180
Press 'q' to cash out or 'r' to continue: q
Thanks for playing!
You cashed out: $180

## Contributing

Feel free to fork the repository, submit issues, or create pull requests to enhance the game (e.g., adding new symbols, payout rules, or a GUI).

## License

This project is open-source and available under the MIT License.

## Contact
For questions, suggestions, or issues, please:

Open an issue on GitHub.

Contact Atharv Sharma at atharvsharmatgu@gmail.com.

This project showcases Python skills, including object-oriented programming, randomization, and game logic. It was built as a fun and educational exercise to simulate a popular card game. Enjoy playing, and may the cards be in your favor!
