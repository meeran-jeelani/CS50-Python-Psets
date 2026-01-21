# prompt user for arithemtic expression
def main():
    expression = input("Expression: ")
    #split expression to 3 parts
    x,y,z = expression.split(" ")
    # convert to float
    x = float(x)
    z = float(z)
    # convert str operator to operator
    operator = str_to_operator(y)

    if operator:
        ans = operator(x, z)
        print(ans)
    else:
        None


import operator

def str_to_operator(o):
    if o == "+":
        return operator.add
    elif o == "-":
        return operator.sub
    elif o == "*":
        return operator.mul
    elif o == "/":
        return operator.truediv
    elif o == "^":
        return operator.xor
    elif o == "%":
        return operator.mod
    else:
        return None


main()
