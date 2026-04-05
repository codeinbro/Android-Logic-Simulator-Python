# NOT Gate Simulator - Simple Version
# Android / Pydroid friendly

def NOT(a):
    """Return output of NOT gate"""
    return 0 if a == 1 else 1

def get_input(prompt):
    """Get valid input 0 or 1 from user"""
    while True:
        val = input(prompt + " (0 or 1): ")
        if val in ['0', '1']:
            return int(val)
        print("Invalid input, please enter 0 or 1.")

print("=== Simple NOT Gate Simulator ===")

while True:
    a = get_input("Input")
    output = NOT(a)
    print(f"Output: {output}")

    cont = input("Try again? (y/n): ").lower()
    if cont != 'y':
        print("Exiting simulator.")
        break