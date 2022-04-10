from Pokemon import Pokemon


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    pok = Pokemon("Schiggy", 1, 40, "Ash")
    nok = Pokemon("Miggy", 1, 40, "Ash")
    pok.showStats()
    nok.showStats()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
