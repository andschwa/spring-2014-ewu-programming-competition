# Team 32

with open("f.in", 'r') as File:
    lines = File.readlines()

programs = []

for line in lines:
    try:
        s = int(line)
        try:
            programs.append(program)
        except:
            None
        program = {}
    except ValueError:
        fields = line.split()
        program[fields.pop(0)] = fields

for program in programs:
    i = min(program.keys())
    visited = set()
    while True:
        statement = program[i][0]
        if statement == "END":
            print("TERMINATES")
            break
        else:
            i = program[i][1]
            if i in visited:
                print("INFINITE LOOP")
                break
            visited.add(i)
