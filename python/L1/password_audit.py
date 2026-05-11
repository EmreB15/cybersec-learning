def audit(password):
    min_12 = len(password) >= 12
    one_upper = False
    one_lower = False
    one_digit = False
    for char in password:
        if one_lower and one_upper and one_digit:
            break
        if char.isupper():
            one_upper = True
        if char.islower():
            one_lower = True
        if char.isdigit():
            one_digit = True

    output_list = []

    if not min_12:
        output_list.append("length")
    if not one_upper:
        output_list.append("uppercase")
    if not one_lower:
        output_list.append("lowercase")
    if not one_digit:
        output_list.append("digit")


    return min_12 and one_upper and one_lower and one_digit , output_list

test_passwords = ["CorrectHorse9Battery", "Short1A", "alllowercase", "PASSWORD"]

for test in test_passwords:
    result, failures = audit(test)
    output = test + ":"
    if result:
        output += " STRONG"
    else:
        output += " WEAK - failed: "
    output += ", ".join(failures)
    print(output)
