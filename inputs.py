print("Exercise 1")
# Q1
prompt = "What is your name? "
name = input(prompt)

print(f"Welcome to Anderson University {name.title()}!")


print("\nExercise 2")
# Q2
prompt = "How much money do you have (in dollars)? "
money = float(input(prompt))

if money < 119.99:
    processor = "i3"
elif money < 199.99:
    processor = "i5"
elif money < 299.99:
    processor = "i7"
else:
    processor = "i9"

print(f"You can afford an Intel {processor} processor.")


print("\nExercise 3")
# Q3
prompt = "Please input an integer: "
prompt += "\n(Enter quit to exit)\n"
value = input(prompt)
while value != "quit":
    if int(value) % 2 == 0:
        print(f"\n{value} is even.\n")
    else:
        print(f"\n{value} is odd.\n")

    value = input(prompt)


print("\nExercise 4")
# Q4
prompt = "Who is the best programmer?:"
prompt += "\nHINT: axelz\n"

is_answer_correct = False
while not is_answer_correct :
    answer = input(prompt)
    if answer.lower() == "quit":
        print("Quitting ...")
        break
    elif answer.lower() != "axelz":
        print("This is the wrong answer\n")
    else:
        print("This is the correct answer")
        is_answer_correct = True


print("\nExercise 5")
# Q5
users = {
        "axelz": "kubuntu",
        "pwrple": "kylin"
        }

prompt = "What is your username?: "
username = input(prompt)

prompt = "What is your favorite ubuntu flavor?: "

flavors = ["kubuntu", "lubuntu", "budgie", "kylin", "mate", "studio", "xubuntu"]

is_answer_correct = False
while not is_answer_correct:
    value = input(prompt)
    if value not in flavors:
        print("\nYou entered a non-legitimate flavor of ubuntu. Here are the options:")
        for flavor in flavors:
            print(f"- {flavor}")
    else:
        users[username] = value
        print("\nHere is our updated list of users:")
        for user, flavor in users.items():
            print(f"- {user}: {flavor}")
        is_answer_correct = True
