import os


def main():
    horizontal = 0
    depth = 0
    data = get_commands()

    for i in range(len(data)):
        command = data[i]
        direction = command.split(" ")[0]
        distance = int(command.split(" ")[1])

        if direction == "forward":
            horizontal += distance
        elif direction == "back":
            horizontal -= distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance

    print(horizontal * depth)


def get_commands():
    os.chdir(os.path.dirname(__file__))
    f = open("input.txt", "r")
    data = [str(item.strip()) for item in f.readlines()]
    f.close
    return data


if __name__ == "__main__":
    main()
