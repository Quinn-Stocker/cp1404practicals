"""
CP1404/CP5632 - Practical

"""

def score_calc (score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"

def main():
    score = float(input("Enter score: "))
    print(score_calc(score))

main()