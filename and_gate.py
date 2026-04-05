# AND Gate Simulator - Simple Version
# Android / Pydroid friendly

def AND(a, b):
    """Return output of AND gate"""
    return a and b

def get_input(prompt):
    """Get valid input 0 or 1 from user"""
    while True:
        val = input(prompt + " (0 or 1): ")
        if val in ['0', '1']:
            return int(val)
        print("Invalid input, please enter 0 or 1.")

print("=== Simple AND Gate Simulator ===")

while True:
    a = get_input("Input A")
    b = get_input("Input B")
    output = AND(a, b)
    print(f"Output: {output}")

    cont = input("Try again? (y/n): ").lower()
    if cont != 'y':
        print("Exiting simulator.")
        break