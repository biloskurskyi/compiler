class Token:
    def __init__(self, math_op):
        self.math_op = math_op

    def operation(self):
        if self.math_op in ['+', '-', '*', '/']:
            return True
        return False

    def priority(self):
        if self.math_op in ['*', "/"]:
            return True
        return False

    def __str__(self):
        return f"{self.math_op}"


R = []

with open("code.txt", "r") as f:
    print()
    print('Phase 1'.center(70))
    code = f.read().replace(" ", "").replace("\n", "").replace("\t",
                                                               "").lower()
    print(code)
    n = 0
    for i in range(len(code)):
        if code[i] in ['>', ';', '=', '*', '/', '+', '-', '[', ']', '(', ')', '{', '}']:
            if i > n:
                R.append(Token(code[n:i]))
            R.append(Token(code[i]))
            n = i + 1

N_C = 0
temp_count = 0
numb = []


def handleExpression(Expression):
    Expression = [Token("(")] + Expression + [Token(")")]
    OP = []
    ARG = []
    add_L = []

    def generateCommand():
        global temp_count
        op = OP.pop().math_op
        rhs = ARG.pop()
        lhs = ARG.pop()
        name = None
        if op == '+':
            name = 'ADD'
        elif op == '-':
            name = 'SUB'
        elif op == '*':
            name = 'MUL'
        elif op == '/':
            name = 'DIV'
        res = "t" + str(temp_count)
        add_L.append(f'{name} {lhs} {rhs} {res}')
        '''for i in add_L:
            print(i)'''
        ARG.append(res)
        temp_count += 1

    while len(Expression) > 0:
        token = Expression.pop(0)

        if token.operation():
            while OP[-1].operation() and OP[-1].priority() >= token.priority():
                generateCommand()
            OP.append(token)
        elif token.math_op == "(":
            OP.append(token)
        elif token.math_op == ")":
            while OP[-1].math_op != "(":
                generateCommand()
            if OP[-1].math_op != "(":
                break
            OP.pop()
        else:
            ARG.append(token)
    while len(OP) > 0:
        if OP[-1].math_op in ["(", ")"]:
            break
        generateCommand()
    return add_L


def hendleOperatorBlock(R1, Ri):
    point1 = Ri
    #print(point1)
    while R1[point1].math_op != "]":
        point1 += 1
    what = handleExpression(R1[Ri + 2:point1])
    '''p = handleComand(R1, R1[0])
    print(p)'''
    #print(len(what))
    #print(what)
    point1 += 2
    point2 = point1
    m = 1
    _ = 0
    for i in range(len(R1)):
        if R1[i].math_op == 'read' or R1[i].math_op == 'write' or R1[i].math_op == '=':
            #print(i)
            _ += 1
    #print(_)
    while m > 0:
        point2 += 1
        if R1[point2].math_op == "{":
            m += 1
        elif R1[point2].math_op == "}":
            m -= 1
    global N_C
    old_n = N_C + 1
    #print(handleBlock(R1[0:point2]))
    #print(R1[point2])
    block = handleBlock(R1[point1:point2])
    #print(len(block))
    N_C += 1
    p = handleComand(R1, 0)
    '''for i in R[:point2]:
        print(i)'''
    #print(block)
    #print(handleBlock(R1[10]))
    global numb
    if R1[Ri].math_op == "if":
        add_L = what + [f"GOTOIFNOT {what[-1].split()[-1]} {len(what)+len(block)+_}"] + handleBlock(R1[point1:point2]) #+ block
        return add_L

    if R[Ri].math_op == "while":
        add_L = what + [f"GOTOIFNOT {what[-1].split()[-1]} {len(what)+len(block)+_}"] + handleBlock(R1[point1:point2]) + [f"GOTO {len(what)+2}"]#+ block
        # add_L = what + [f"GOTO {old_n}"]
        return add_L


def handleComand(R, Ri):
    add_L = []
    if R[Ri].math_op == "read":
        add_L.append("READ " + R[Ri + 2].math_op)
    elif R[Ri].math_op == "write":
        add_L.append("WRITE " + R[Ri + 2].math_op)
    else:
        point = Ri + 1
        while R[point].math_op != ';':
            point += 1
        if point - Ri == 2:
            add_L.append(f"COPY {R[Ri - 1].math_op} {R[Ri + 1].math_op}")
        else:
            add_L = handleExpression(R[Ri + 1:point])
            add_L[-1] = add_L[-1].replace(add_L[-1].split()[-1], R[Ri - 1].math_op)
    return add_L


def handleBlock(R, Ri=0):
    L = []
    while (Ri < len(R)):
        if R[Ri].math_op in ["while", "if"]:
            #print(hendleOperatorBlock(R, Ri))
            rez = hendleOperatorBlock(R, Ri)
            L += rez
            break

        elif R[Ri].math_op in ["read", "write", "="]:
            rez = handleComand(R, Ri)
            L += rez
        Ri += 1
    global N_C
    N_C += len(L)
    return L


L = handleBlock(R)
print()
print('Phase 2'.center(70))
k = 0
#print(L[:3])
for i in range(len(L)):
    print(i, L[i])
    numb.append(L[i].split())
    k = i
# print(numb)
with open("wf.txt", "w") as f:
    for i in range(len(L)):
        f.write(L[i])
        f.write('\n')
f.close()
'''print(
1 READ a
2 READ e
3 COPY x 1
4 DIV a x t0
5 SUB x t0 t1
6 DIV a x t2
7 SUB x t2 t3
8 MUL t1 t3 t4
9 MUL 4 e t5
10 MUL t5 e t6
11 SUB t4 t6 t7
12 GOTOIFNOT t7 17
13 DIV a x t8
14 ADD x t8 t9
15 MUL 0.5 t9 x
16 WRITE x
17 GOTO 10)'''
'''def handleOperatorBlock(it):
    is_loop = False
    if str(it.value().sym) == "while":
        is_loop = True
    it.next()
    if str(it.value().sym) != "[":
        raise SyntaxError()
    it.next()
    res = handleExpression(it)

    begin = len(c)
    com = Command("GOTOIFNOT", res.args[-1], None)
    c.append(com)

    if str(it.value().sym) != "{":
        raise SyntaxError()
    it.next()

    handleBlock(it)

    if str(it.value().sym) != "}":
        raise SyntaxError()
    it.next()

    if is_loop:
        c.append(Command("GOTO", begin - 1))
    com.ptr = len(c)'''
