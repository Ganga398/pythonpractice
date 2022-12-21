"""
camelcase = input("camelcase: ")
snake_case = ""
for i in range(len(camelcase)):
    if camelcase[i].isupper():
        snake_case = snake_case + '_' + camelcase[i].lower()
    else:
        snake_case += camelcase[i]
print("snake _case :", snake_case)
"""


camelcase = input("camelcase: ")
print("snake_case: ", end="")
for letter in camelcase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")
