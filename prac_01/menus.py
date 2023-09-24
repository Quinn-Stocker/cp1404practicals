# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message

name = str(input("Enter name: "))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = str(input(">> "))

while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("invalid input")

    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = str(input(">> "))

print("Finished.")