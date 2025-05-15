import ast  # Module to parse and analyze Abstract Syntax Trees (ASTs) in Python.
import sys  # Module providing access to system-level functionality.
import traceback  # Module to handle and format exceptions for debugging.

# Prompt symbol for user interaction
PROMPT = "\N{snake} "  # Unicode snake emoji (🐍) as a prompt symbol.


# Class to define command constants for better readability and maintainability.
class Command:
    HELP = "help"  # Command to display help information.
    EXIT = "exit"  # Command to exit the REPL.
    QUIT = "quit"  # An alternative command to exit the REPL.


# Function to check the validity of the provided Python code.
def valid(code, mode):
    """
    Validates Python code by parsing it in the given mode.

    Args:
    code (str): The code to validate.
    mode (str): Specifies the mode for parsing; "eval" for expressions, "exec" for statements.

    Returns:
    bool: True if code is valid Python syntax, False otherwise.
    """
    try:
        ast.parse(code, mode=mode)  # Parse the code using the given mode.
        return True  # Code is valid if no exceptions are raised.
    except SyntaxError:
        return False  # Code is invalid due to a syntax error.


# Main function implementing a Python REPL (Read-Eval-Print Loop).
def main():
    """
    Starts a simple Python REPL (Read-Eval-Print Loop) with custom commands.
    """
    # Display initial REPL help message.
    print('Type "help" for more information, "exit" or "quit" to finish.')

    while True:  # Keep running the REPL until explicitly exited.
        try:
            # Read user input and handle it based on the command or code entered.
            match input(PROMPT):  # Replace PROMPT with the snake emoji symbol.
                case Command.HELP:  # Help command: Display Python version info.
                    message = f"Python {sys.version}"  # Get the current Python version.
                    print(message)

                case Command.EXIT | Command.QUIT:  # Exit command: Close the REPL.
                    break  # Exit the loop, terminating the REPL.

                # Handle valid Python expressions (evaluated with `eval`).
                case expression if valid(expression, "eval"):
                    _ = eval(expression)  # Evaluate the expression.
                    if _ is not None:  # Print the result if not `None`.
                        print(_)

                # Handle valid Python statements (executed with `exec`).
                case statement if valid(statement, "exec"):
                    exec(statement)  # Execute the Python statement.

                # If input does not match any valid commands or code.
                case _:
                    print("Please type a command")  # Prompt the user for valid input.

        # Handle user interruption with Ctrl+C.
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")  # Inform the interruption and continue.

        # Handle EOF (End of File) such as Ctrl+D.
        except EOFError:
            print()  # Print a newline for clean output.
            exit()  # Exit the REPL gracefully.

        # Handle any other type of exception during runtime (e.g., name error).
        except Exception:
            traceback.print_exc(file=sys.stdout)  # Display the traceback for debugging.


# Ensure the script runs only when executed directly, not when imported.
if __name__ == "__main__":
    main()
