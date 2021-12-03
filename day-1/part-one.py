import os


def main():
    count: int = 0
    data: list = get_readings()
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            count += 1
    print(count)


def get_readings(filename: str = "input.txt") -> list:
    os.chdir(os.path.dirname(__file__))
    with open(filename, "r", encoding="utf-8") as file:
        data = [int(item) for item in file.readlines()]
    return data


if __name__ == "__main__":
    main()
