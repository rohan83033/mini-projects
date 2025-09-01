import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        row_symbols = []
        for col in columns:
            row_symbols.append(col[row])
        print(" | ".join(row_symbols))


def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def deposit():
    while True:
        amount = input("Enter amount to deposit: ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")


def get_bet():
    while True:
        bet = input(f"Enter bet amount per line ({MIN_BET}-{MAX_BET}): ₹")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Bet must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient balance! Your current balance is ₹{balance}.")
        else:
            break

    print(f"\nYou are betting ₹{bet} on {lines} lines. Total bet = ₹{total_bet}\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print("----- SPIN RESULT -----")
    print_slot_machine(slots)

    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)

    balance -= total_bet
    balance += winnings

    net_change = winnings - total_bet
    print("\n----- ROUND SUMMARY -----")
    print(f"Total Bet: ₹{total_bet}")
    print(f"Winnings: ₹{winnings}")
    print(f"Net Change: {'+' if net_change > 0 else ''}{net_change}")
    if winning_lines:
        print(f"Winning Lines: {', '.join(map(str, winning_lines))}")
    else:
        print("No winning lines this round.")
    print(f"Updated Balance: ₹{balance}\n")

    return balance


def main():
    balance = deposit()
    while True:
        print(f"Current balance: ₹{balance}")
        choice = input("Press Enter to spin (or 'q' to quit): ")
        if choice.lower() == "q":
            break
        balance = spin(balance)

        if balance <= 0:
            print("You ran out of money. Game Over!")
            break

    print(f"\nYou left with ₹{balance}. Thanks for playing!")


main()
