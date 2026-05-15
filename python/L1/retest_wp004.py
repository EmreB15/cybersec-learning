failed_users = []

with open(r"D:\cybersecurity_learning\labs\bash-L1\retest-wp002-r2\auth-snippet.log") as f:
    for line in f:
        user = line.split()[10]
        if ('Failed' in line) and (user not in failed_users):
            failed_users.append(user)
    print(len(failed_users))
