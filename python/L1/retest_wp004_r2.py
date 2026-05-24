with open(r'labs\python-L1\wp004-retest-r2\auth-snippet.log') as f:
    dates = []
    for line in f:
        if 'Failed' in line:
            dates.append(" ".join(line.split(" ")[:3]))
    print("first failed: " + dates[0])
    print("Last failed: " + dates[-1])
