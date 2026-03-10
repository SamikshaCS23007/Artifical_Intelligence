# Define maximum capacities
CAP_X = 4
CAP_Y = 3

# Global variables for jug states
x = 0  # 4-gallon jug
y = 0  # 3-gallon jug

# Function to display the current state
def print_state():
    print(f"Current State: ({x}, {y})")

# Function to apply production rules
# Returns True if the rule was applied successfully, False otherwise
def apply_rule(rule):
    global x, y
    
    # RULE 1: Fill 4-gallon jug
    if rule == 1:
        if x < CAP_X:
            x = CAP_X
            print("Rule 1 applied: Fill 4-gallon jug.")
            return True

    # RULE 2: Fill 3-gallon jug
    elif rule == 2:
        if y < CAP_Y:
            y = CAP_Y
            print("Rule 2 applied: Fill 3-gallon jug.")
            return True

    # RULE 3: Empty 4-gallon jug
    elif rule == 3:
        if x > 0:
            x = 0
            print("Rule 3 applied: Empty 4-gallon jug.")
            return True

    # RULE 4: Empty 3-gallon jug
    elif rule == 4:
        if y > 0:
            y = 0
            print("Rule 4 applied: Empty 3-gallon jug.")
            return True

    # RULE 5: Pour 3-gallon into 4-gallon until 4-gallon is full
    elif rule == 5:
        if (x + y >= CAP_X) and (y > 0):
            amount_needed = CAP_X - x
            y = y - amount_needed
            x = CAP_X
            print("Rule 5 applied: Pour 3-gal into 4-gal until full.")
            return True

    # RULE 6: Pour 4-gallon into 3-gallon until 3-gallon is full
    elif rule == 6:
        if (x + y >= CAP_Y) and (x > 0):
            amount_needed = CAP_Y - y
            x = x - amount_needed
            y = CAP_Y
            print("Rule 6 applied: Pour 4-gal into 3-gal until full.")
            return True

    # RULE 7: Pour all water from 3-gallon into 4-gallon
    elif rule == 7:
        if (x + y <= CAP_X) and (y > 0):
            x = x + y
            y = 0
            print("Rule 7 applied: Pour all 3-gal into 4-gal.")
            return True

    # RULE 8: Pour all water from 4-gallon into 3-gallon
    elif rule == 8:
        if (x + y <= CAP_Y) and (x > 0):
            y = x + y
            x = 0
            print("Rule 8 applied: Pour all 4-gal into 3-gal.")
            return True

    # RULE 9: Special Case - Pour 2 gallons from 3-gal to 4-gal (Target Step)
    elif rule == 9:
        if x == 0 and y == 2:
            x = 2
            y = 0
            print("Rule 9 applied: Pour 2 gallons from 3-gal to 4-gal.")
            return True

    # RULE 10: Special Case - Empty 2 gallons from 4-gal (if needed)
    elif rule == 10:
        if x == 2:
            x = 0
            print("Rule 10 applied: Empty 2 gallons from 4-gal.")
            return True

    # RULE 11: Special Case - Pour 4-gal into 3-gal leaving remainder (Special variant of Rule 6)
    elif rule == 11:
        if x == 4 and y == 0:
            x = 1
            y = 3
            print("Rule 11 applied: Special Pour 4->3 leaving 1 in 4.")
            return True

    # RULE 12: Special Case - Empty 3-gal jug to ground specifically when 4-gal is full
    elif rule == 12:
        if x == 4 and y > 0:
            y = 0
            print("Rule 12 applied: Empty 3-gal while 4-gal is full.")
            return True

    print(f"Rule {rule} cannot be applied to state ({x}, {y})")
    return False

# Main execution block
if __name__ == "__main__":
    print("Water Jug Problem Solver")
    print("Initial State: (0, 0)")
    print("Goal State: (2, 0)\n")

    # Solution Sequence
    solution_sequence = [2, 7, 2, 5, 3, 9]

    for rule in solution_sequence:
        if apply_rule(rule):
            print_state()
            if x == 2:
                print("\nSUCCESS: Goal state (2, n) reached!")
                break
        else:
            print("Error applying sequence.")
            break
        print("-----------------------------")