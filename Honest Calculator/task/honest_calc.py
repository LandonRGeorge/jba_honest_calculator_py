import operator
import typing

opers = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
memory = 0


def get_nbr(val: str) -> float:
    if val == "M":
        return float(memory)
    return float(val)


def is_one_digit(val: float) -> bool:
    return abs(val) < 10 and val.is_integer()


def check(v1: float, v2: float, op: str) -> None:
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and op == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and op in ["*", "+", "-"]:
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
    return


while True:
    print("Enter an equation")
    x, oper, y = input().split(" ")

    try:
        x = get_nbr(x)
        y = get_nbr(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue

    try:
        oper_func = opers[oper]
    except KeyError:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    check(x, y, oper)

    try:
        result = oper_func(x, y)
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
        continue

    print(result)

    store_initial_answer = input("Do you want to store the result? (y / n):\n")
    if store_initial_answer == "y":
        if is_one_digit(result):
            msgs = [
                "Are you sure? It is only one digit! (y / n)",
                "Don't be silly! It's just one number! Add to the memory? (y / n)",
                "Last chance! Do you really want to embarrass yourself? (y / n)",
            ]
            store_additional_answer = "n"
            for msg in msgs:
                store_additional_answer = input(msg + "\n")
                if store_additional_answer == "n":
                    break
            if store_additional_answer == "y":
                memory = result
        else:
            memory = result

    cont = input("Do you want to continue calculations? (y / n):\n")
    if cont == "y":
        continue

    break
