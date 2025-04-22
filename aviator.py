import random
import time

def generate_crash_point():
    """Generates a random crash multiplier based on probability distribution."""
    # The higher the multiplier, the less likely it is
    r = random.random()
    if r < 0.5:
        return round(random.uniform(1.0, 2.0), 2)
    elif r < 0.8:
        return round(random.uniform(2.0, 5.0), 2)
    elif r < 0.95:
        return round(random.uniform(5.0, 10.0), 2)
    else:
        return round(random.uniform(10.0, 50.0), 2)

def play_game():
    crash_point = generate_crash_point()
    multiplier = 1.0
    increment = 0.01
    print("\n✈️ Plane taking off...\n")

    while multiplier < crash_point:
        print(f"🚀 Multiplier: x{multiplier:.2f}")
        time.sleep(0.1)
        multiplier += increment + (multiplier * 0.01)  # simulate acceleration

        # simulate user action (replace with input or AI logic)
        if multiplier >= 2.0:
            print(f"\n💰 You cashed out at x{multiplier:.2f}!")
            return

    print(f"\n💥 CRASH at x{crash_point:.2f}! You lost.")

# Run the game
while True:
    play_game()
    again = input("\nPlay again? (y/n): ")
    if again.lower() != 'y':
        break
print("Thanks for playing!")