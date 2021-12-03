def main():
    count = 0
    data = get_readings()
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            count += 1
    print(count)


def get_readings():
    f = open("input.txt", "r")
    data = [int(item) for item in f.readlines()]
    f.close
    return data


if __name__ == "__main__":
    main()
