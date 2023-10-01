def main():
    def get_password():
        min_length = 4
        correct_input = False
        while correct_input == False:
            password = str(input("Enter Password: "))
            if len(password) >= min_length:
                correct_input = True

        return password
    password = get_password()
    def pass_hider(password):
        hidden_pass = ""
        for i in range(0, len(password), 1):
            hidden_pass = hidden_pass + "*"

        print(hidden_pass)
    pass_hider(password)

main()