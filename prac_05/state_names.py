"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for state_key in CODE_TO_NAME:
    print(f"{state_key:<3} is {CODE_TO_NAME[state_key]}")

state_code = str(input("Enter short state: "))
while state_code != "":
    
    # if state_code.upper() in CODE_TO_NAME:
    #     print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    # else:
    #     print("Invalid short state")

    try:
        print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    except KeyError:
        print("Invalid Short State")

    state_code = str(input("Enter short state: "))