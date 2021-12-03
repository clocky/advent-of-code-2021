def main():
    horizontal = 0
    depth = 0
    aim = 0
    data = get_commands()

    for i in range(len(data)):
        command = data[i]
        direction = command.split(" ")[0]
        units = int(command.split(" ")[1])

        if direction == "down":
            aim += units
        elif direction == "up":
            aim -= units
        elif direction == "forward":
            horizontal += units
            depth += (aim * units)

    print(horizontal * depth)


def get_commands():
    f = open("input.txt", "r")
    data = [str(item.strip()) for item in f.readlines()]
    f.close
    return data


if __name__ == "__main__":
    main()
