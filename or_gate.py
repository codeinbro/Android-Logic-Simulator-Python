# OR Gate Simulator - Simple Version
# Android / Pydroid friendly

def OR(a, b):
    """Return output of OR gate"""
    return a or b

def get_input(prompt):
    """Get valid input 0 or 1 from user"""
    while True:
        val = input(prompt + " (0 or 1): ")
        if val in ['0', '1']:
            return int(val)
        print("Invalid input, please enter 0 or 1.")

print("=== Simple OR Gate Simulator ===")

while True:
    a = get_input("Input A")
    b = get_input("Input B")
    output = OR(a, b)
    print(f"Output: {output}")

    cont = input("Try again? (y/n): ").lower()
    if cont != 'y':
        print("Exiting simulator.")
        break