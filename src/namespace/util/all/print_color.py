def print_color(text, color):
    colors = {
        'red': '\033[91m',
        'orange': '\033[38;5;208m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'green': '\033[92m',
        'purple': '\033[95m',
        'reset': '\033[0m'
    }

    if color in colors:
        print(f"{colors[color]}{text}{colors['reset']}")
    else:
        print(text)