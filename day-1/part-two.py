import os


def main():
    count = 0
    data = get_readings()
    windows = create_windows(data)

    for i in range(len(windows) - 1):
        if windows[i] < windows[i + 1]:
            count += 1
    print(count)


def create_windows(data):
    windows = []
    for i in range(len(data) - 1):
        windows.append(sum(data[i:i + 3]))
    return windows


def get_readings():
    os.chdir(os.path.dirname(__file__))
    f = open("input.txt", "r")
    data = [int(item) for item in f.readlines()]
    f.close
    return data


if __name__ == "__main__":
    main()
