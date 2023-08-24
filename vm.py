lines = []
with open("wf.txt", "r") as f:
    for i in f.readlines():
        lines.append(i.split())
'''for i in lines:
    print(i)'''
mem = {}
i = 0
# print(len(lines))
while i < len(lines):
    if lines[i][0] == 'READ':
        input_ = float(input(">"))
        mem.update({lines[i][1]: input_})

    elif lines[i][0] == 'ADD':
        if lines[i][1] in mem:
            a = mem[lines[i][1]]
        else:
            a = float(lines[i][1])
        if lines[i][2] in mem:
            b = mem[lines[i][2]]
        else:
            b = float(lines[i][2])
        mem.update({lines[i][3]: float(a) + float(b)})

    elif lines[i][0] == 'SUB':
        if lines[i][1] in mem:
            a = mem[lines[i][1]]
        else:
            a = float(lines[i][1])
        if lines[i][2] in mem:
            b = mem[lines[i][2]]
        else:
            b = float(lines[i][2])
        mem.update({lines[i][3]: float(a) - float(b)})

    elif lines[i][0] == 'MUL':
        if lines[i][1] in mem:
            a = mem[lines[i][1]]
        else:
            a = float(lines[i][1])
        if lines[i][2] in mem:
            b = mem[lines[i][2]]
        else:
            b = float(lines[i][2])
        mem.update({lines[i][3]: float(a) * float(b)})

    elif lines[i][0] == 'DIV':
        if lines[i][1] in mem:
            a = mem[lines[i][1]]
        else:
            a = float(lines[i][1])
        if lines[i][2] in mem:
            b = mem[lines[i][2]]
        else:
            b = float(lines[i][2])
        mem.update({lines[i][3]: float(a) / float(b)})

    elif lines[i][0] == 'COPY':
        mem.update({lines[i][1]: lines[i][2]})

    elif lines[i][0] == 'WRITE':
        print(mem[lines[i][1]])

    elif lines[i][0] == 'GOTOIFNOT':
        if abs(mem[lines[i][1]]) <= 0.1 and bool(int(mem[lines[i][1]])) is False:
            i = int(lines[i][2]) - 1

    elif lines[i][0] == 'GOTO':
        i = int(lines[i][1])
    i += 1



    '''elif '#' in lines[i][0]:
        line = lines[i][0].split("#")
        if line[0] in mem:
            mem.update({line[1]: lines[i][1]})
        else:
            mem.update({line[0]: {}})
            mem[line[0]].update({line[1]: lines[i][1]})'''

'''print('-')
a = 64
e = 0.1
x = 1
while (x-a/x)*(x-a/x)-4*e*e:
    x = 0.5 * (x + a / x)
    print(x)'''