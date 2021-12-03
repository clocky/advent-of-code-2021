import os


def main():
    horizontal: int = 0
    depth: int = 0
    aim: int = 0
    commands: list = get_commands()

    for command in commands:
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


def get_commands(filename: str = "input.txt") -> list:
    os.chdir(os.path.dirname(__file__))
    with open(filename, "r", encoding="utf-8") as file:
        data = [str(item.strip()) for item in file.readlines()]
    return data


if __name__ == "__main__":
    main()