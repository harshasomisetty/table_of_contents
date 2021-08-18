with open("g.txt", "r") as file:
    lines = [line.rstrip() for line in file if line.rstrip()]
    print(len(lines))
