def main():
    email = str(input("Email: "))

    name_to_email = {}

    while email != "":
        guessed_name = name_extractor(email)
        
        name_check = str(input(f"Is your name {guessed_name}? (Y/n) "))

        if name_check.upper() == "Y" or name_check == "":
            name_to_email[guessed_name] = email
        else:
            name_to_email[str(input("Name: "))] = email

        email = str(input("Email: "))

    print("")

    for name in name_to_email:
        print(f"{name} ({name_to_email[name]})")

def name_extractor(email):

    # single line version, wasn't sure if I could do this so just split it up
    # return (" ".join((email.split("@")[0])[0].split("."))).title()

    username = email.split("@")[0]

    username = username.split(".")

    guessed_name = " ".join(username).title()

    return guessed_name

main()