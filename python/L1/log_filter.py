with open("labs/bash-L1/retest-wp002/auth-snippet.log") as f:
    for line in f:
        if "Failed" in line:
            print(line, end="")
