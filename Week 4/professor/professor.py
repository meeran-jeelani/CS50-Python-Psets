import random

def main():
    l = get_level()

    count = 0
    score = 0
    wrong = 0

    while True:
        while count < 10:
            x = generate_integer(l)
            y = generate_integer(l)

            ans = x + y
            print(f"{x} + {y} = ", end="")

            count += 1

            while True:
                if wrong == 3:
                    print(ans)
                    wrong = 0
                    break
                try:
                    my_ans = int(input())
                except ValueError:
                    wrong += 1
                    print("EEE")
                    print(f"{x} + {y} = ", end="")
                else:
                    if my_ans == ans:
                        score += 1
                        break
                    else:
                        wrong += 1
                        print("EEE")
                        print(f"{x} + {y} = ", end="")
        else:
            print(f"Score: {score}")
            break

def get_level():
    valid = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in valid:
                return level

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    if level == 1:
        num = random.randint(0,9)
    elif level == 2:
        num = random.randint(10,99)
    else:
        num = random.randint(100,999)
    return num

if __name__ == "__main__":
    main()
