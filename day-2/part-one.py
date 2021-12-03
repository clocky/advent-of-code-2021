import os


def main():
    horizontal: int = 0
    depth: int = 0
    data: list = get_commands()

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


def get_commands(filename: str = "input.txt") -> list:
    os.chdir(os.path.dirname(__file__))
    with open(filename, "r") as file:
        data = [str(item.strip()) for item in file.readlines()]
    return data


if __name__ == "__main__":
    main()
