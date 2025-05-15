import sys
import traceback

PROMPT = "\N{snake} "

class Command:
    HELP = "help"
    EXIT = "exit"
    QUIT = "quit"


def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case Command.HELP:
                    message = f"Python {sys.version}"
                    print(message)
                case Command.EXIT:
                    break
                case Command.QUIT:
                    break
                case _:
                    print("Please type a command")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    main()