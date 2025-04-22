import random
import time

def rigged_crash_point(bet_amount, balance):
    """
    Simulates a rigged crash point:
    - Big bet = earlier crash
    - Low balance = higher crash
    - Bet over threshold = force early crash
    """
    base = 1.0

    if bet_amount > 1000:
        return round(random.uniform(1.0, 1.5), 2)

    if balance < 500:
        return round(random.uniform(5.0, 20.0), 2)

    # Normal case
    r = random.random()
    if r < 0.5:
        return round(random.uniform(1.0, 2.0), 2)
    elif r < 0.8:
        return round(random.uniform(2.0, 5.0), 2)
    else:
        return round(random.uniform(5.0, 10.0), 2)

def play_rigged_game(balance):
    bet = float(input(f"\n💰 Your balance: KSh {balance:.2f}\nEnter bet amount: KSh "))
    if bet > balance:
        print("❌ Insufficient funds.")
        return balance

    crash_point = rigged_crash_point(bet, balance)
    multiplier = 1.0
    print("\n✈️ Plane taking off...\n")

    while multiplier < crash_point:
        print(f"🚀 Multiplier: x{multiplier:.2f}")
        time.sleep(0.1)
        multiplier += 0.01 + (multiplier * 0.01)

        # Simulate player cash out (auto at x2.0)
        if multiplier >= 2.0:
            print(f"\n✅ Cashed out at x{multiplier:.2f}! You win KSh {bet * multiplier:.2f}")
            return balance - bet + (bet * multiplier)

    print(f"\n💥 CRASHED at x{crash_point:.2f}! You lost KSh {bet:.2f}")
    return balance - bet

# 🔁 Run it
balance = 2000.0
while balance > 0:
    balance = play_rigged_game(balance)
    again = input("\nPlay again? (y/n): ")
    if again.lower() != 'y':
        break

print(f"\n🏁 Final Balance: KSh {balance:.2f}")
print("Thanks for playing!")