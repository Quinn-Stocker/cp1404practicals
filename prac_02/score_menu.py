menu = "(G)et a valid score (0-100)\r\n(P)rint result\r\n(S)how stars\r\n(Q)uit\r\n"

def get_score():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("invalid score")
    else:
        return score

def print_result(score):
    if score > 90:
        return "Excellent: " + str(score)
    elif score > 50:
        return "Passable: " + str(score)
    else:
        return "Bad: " + str(score)

def print_stars(score):
    star_print = ""
    for i in range(0, int(score), 1):
        star_print = star_print + "*"

    print(star_print)

def main():
    print(menu)
    choice = str(input("Choice: "))
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(print_result(score))
        elif choice == "S":
            print(print_stars(score))
        else:
            print("invalid input")
        print(menu)
        choice = str(input("Choice: "))
    print("farewell")

main()