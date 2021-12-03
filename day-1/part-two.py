import os


def main():
    count: int = 0
    data: list = get_readings()
    windows: list = create_windows(data)

    for i in range(len(windows) - 1):
        if windows[i] < windows[i + 1]:
            count += 1
    print(count)


def create_windows(data: list) -> list:
    windows = []
    for i in range(len(data) - 1):
        windows.append(sum(data[i:i + 3]))
    return windows


def get_readings(filename: str = "input.txt") -> list:
    os.chdir(os.path.dirname(__file__))
    with open(filename, "r") as file:
        data = [int(item) for item in file.readlines()]
    return data


if __name__ == "__main__":
    main()
