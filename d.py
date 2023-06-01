import os
import sys
import time
from colorama import init, Fore, Style

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def print_colored_text(text, color):
    print(color + text + Style.RESET_ALL, end='')

def print_large_letter(letter):
    clear_console()
    init()

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    if letter == 'M':
        character = [
            "MM               MM",
            "MM M          M MM",
            "MM   M       M   MM",
            "MM     M    M     MM",
            "MM       M M       MM",
            "MM         M         MM",
            "MM                   MM",
            "MM                   MM",
            "MM                   MM",
            "MM                   MM",
            "MM                   MM",
            "MM                   MM",
            "MM                   MM"
        ]
    elif letter == 'I':
        character = [
            "IIIIIIIIII",
            "     II",
            "     II",
            "     II",
            "     II",
            "     II",
            "     II",
            "     II",
            "IIIIIIIIII"
        ]
    elif letter == 'K':
        character = [
            "KK        KK",
            "KK      KK",
            "KK    KK",
            "KK  KK",
            "KKKK",
            "KK  KK",
            "KK    KK",
            "KK      KK",
            "KK        KK"
        ]
    elif letter == 'E':
        character = [
            "EEEEEEEEEE",
            "EE",
            "EE",
            "EEEEEE",
            "EE",
            "EE",
            "EE",
            "EE",
            "EEEEEEEEEE"
        ]
    else:
        character = []

    rotation = 0
    while rotation < 360:
        clear_console()

        for i, row in enumerate(character):
            for char in row:
                color = colors[(i + rotation) % len(colors)]
                print_colored_text(char, color)
            print()

        rotation += 10
        time.sleep(0.05)

    time.sleep(1)

print_large_letter('M')
print_large_letter('I')
print_large_letter('K')
print_large_letter('E')
