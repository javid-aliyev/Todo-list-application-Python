import colorama as col

### COLORAMA FUNCTIONS
def make_green():
    print(col.Fore.GREEN)
def make_red():
    print(col.Fore.RED)
def make_blue():
    print(col.Fore.BLUE)
def print_green(t): # t -> text
    print(col.Fore.GREEN + t)
def print_red(t):
    print(col.Fore.RED + t)
def print_red_resetall(t):
    print(col.Fore.RED + t + col.Style.RESET_ALL)
def print_blue(t):
    print(col.Fore.BLUE + t)
def resetall():
    print(col.Style.RESET_ALL)
