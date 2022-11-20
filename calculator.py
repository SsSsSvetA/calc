def priority(z):
    if z in ['×', '*', '/']:
        return 2
    elif z in ['+', '-']:
        return 1


def in2post(expr):
    stack = []
    post = []
    for z in expr:
        if z not in ['×', '*', '/', '+', '-', '(', ')']:
            post.append(z)
        else:
            if z != ')' and (not stack or z == '(' or stack[-1] == '('
                             or priority(z) > priority(stack[-1])):
                stack.append(z)
            elif z == ')':
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
                    else:
                        break
            else:
                while True:
                    if stack and stack[-1] != '(' and priority(z) <= priority(stack[-1]):
                        post.append(stack.pop())
                    else:
                        stack.append(z)
                        break
    while stack:
        post.append(stack.pop())
    return post


if __name__ == '__main__':
    s = input()
    post = in2post(s)
    print('Постфиксное выражение:', post)

ResultList = []

for i in post:
    if i.isdigit():
        ResultList.append(int(i))
        continue
    op1, op2 = ResultList.pop(), ResultList.pop()
    if i == '+':
        ResultList.append(op2 + op1)
    elif i == '-':
        ResultList.append(op2 - op1)
    elif i == '*' or i == '×':
        ResultList.append(op2 * op1)
    elif i == '/':
        ResultList.append(op2 / op1)
print(ResultList)


