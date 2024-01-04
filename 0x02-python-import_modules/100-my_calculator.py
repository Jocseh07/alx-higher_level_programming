#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    from calculator_1 import add, div, mul, sub

    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    print(sys.argv[2])
    b = int(sys.argv[3])
    total = 0
    if sys.argv[2] == "+":
        total = add(a, b)
    elif sys.argv[2] == "-":
        total = sub(a, b)
    elif sys.argv[2] == "*":
        total = mul(a, b)
    elif sys.argv[2] == "/":
        total = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")

    print("{} {} {} = {}".format(a, sys.argv[2], b, total))
