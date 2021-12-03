""" Day 3: Binary Diagnostic """
import os


def main():
    """ Calculate power consumption from Gamma and Epsilon values"""
    gamma_rate: int = 0
    epsilon_rate: int = 0
    power_consumption: int = 0
    data: list = get_report()

    gamma_rate = get_gamma(data)
    epsilon_rate = get_epsilon(data)
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)


def get_gamma(data: list) -> str:
    """ Returns the gamma value """
    gamma: str = ""

    for column in range(0, 12):
        zero: int = 0
        ones: int = 0
        for binary in data:
            if binary[column] == '1':
                ones += 1
            else:
                zero += 1
        gamma += "0" if (zero > ones) else "1"

    return int(gamma, 2)


def get_epsilon(data: list) -> str:
    """ Returns the epsilon value """
    epsilon: str = ""

    for column in range(0, 12):
        zero: int = 0
        ones: int = 0
        for binary in data:
            if binary[column] == '1':
                ones -= 1
            else:
                zero -= 1
        epsilon += "0" if (zero > ones) else "1"

    return int(epsilon, 2)


def get_report(filename: str = "input.txt") -> list:
    """ Reads the input file and returns a list of binary readings """
    os.chdir(os.path.dirname(__file__))
    with open(filename, "r", encoding="utf-8") as file:
        data = [str(item) for item in file.readlines()]
    return data


if __name__ == "__main__":
    main()
