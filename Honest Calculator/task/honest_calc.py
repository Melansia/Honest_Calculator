messages = {
    "msg_0": "Enter an equation",
    "msg_1": "Do you even know what numbers are? Stay focused!",
    "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "msg_3": "Yeah... division by zero. Smart move...",
    "msg_4": "Do you want to store the result? (y / n):",
    "msg_5": "Do you want to continue calculations? (y / n):",
    "msg_6": " ... lazy",
    "msg_7": " ... very lazy",
    "msg_8": " ... very, very lazy",
    "msg_9": "You are",
    "msg_10": "Are you sure? It is only one digit! (y / n)",
    "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)",
}


def main():
    MEMORY = 0

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    while True:
        read_calc = input(f"{messages['msg_0']}\n").lstrip()

        x, oper, y = read_calc.split(' ')

        try:
            x = float(x) if x != "M" else MEMORY
            y = float(y) if y != "M" else MEMORY
            if oper in ["+", "-", "*", "/"]:
                check(x, y, oper)
                if oper == "/" and y == 0:
                    print(messages['msg_3'])
                else:
                    result = operations[oper](x, y)
                    print(result)
                    store_calculation = input(f"{messages['msg_4']}\n")

                    if store_calculation.lower() == "y":
                        if is_one_digit(result):
                            msg_index = 10
                            while True:
                                question = messages[f"msg_{msg_index}"]
                                answer = input(f"{question}\n")
                                if answer.lower() == "n":
                                    break
                                elif answer.lower() == "y" and not msg_index < 12:
                                    MEMORY = result
                                    break
                                else:
                                    msg_index += 1
                        else:
                            MEMORY = result

                    continue_calculation = input(f"{messages['msg_5']}\n")
                    if continue_calculation.lower() == "y":
                        continue
                    else:
                        break

            else:
                print(messages['msg_2'])
        except ValueError:
            print(messages['msg_1'])


def check(v1, v2, v3):
    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages["msg_6"]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += messages["msg_7"]
    if (v1 == 0 or v2 == 0) and v3 in ["+", "-", "*"]:
        msg += messages["msg_8"]
    if msg != "":
        msg = messages["msg_9"] + msg
        print(msg)
    else:
        pass


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


if __name__ == '__main__':
    main()
