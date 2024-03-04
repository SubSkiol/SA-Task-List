"""Load, save, and manage tasks inside of a task list.
This base should be used for both CLI and GUI varients of the Task List."""
import json
from colorama import Fore, Back, Style, init

# Start json section 
def load_json():
    """Load data from the JSON file."""

    try:
        with open("list_data.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            print(f"Loaded Data")
        return data
    except FileNotFoundError:
        print(f"{Fore.BLACK}{Back.YELLOW}No existing data file found.{Style.RESET_ALL}")
        input()
        return dict()

def save_json(data):
    """Save current instance of the task list. 
    This should print the list then ask for confirmation before overwriting the JSON."""

    view_list(data)
    print(f"{Fore.YELLOW}Are you sure you wish to save? This will overwrite the file.")
    save_confirmation = input(f"{Fore.RED}Y/n\n{Fore.RESET}").lower()

    if save_confirmation == "y" or "": # Yes is the default option
        with open("list_data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2)
        print(f"Saved Data")
        input()


# Start List management section
def add_to_list(t_list):
    """Handle instances of adding to the task list"""

    add_loop = True
    while add_loop:
        print(f"{Fore.YELLOW}Enter a unique name (key) for your task\n",
              "Warning: If the key already exists, data will be overwritten")
        user_key = input(f"{Fore.RED}Press Q to quit\n{Fore.RESET}")
        if user_key.lower() == "q":
            add_loop = False
        else:
            print(f"{Fore.YELLOW}Task name is {Fore.MAGENTA}'{user_key}'{Fore.RESET}")

            user_value = input(f"{Fore.RED}Type the task\n{Fore.RESET}")

            try:
                t_list[user_key] = user_value
                print(f"{Fore.MAGENTA}Added task!{Fore.RESET}",
                        {t_list[user_key]})
                add_loop = False
            except KeyError as e:
                print(f"{Fore.BLACK}{Back.YELLOW}Key error: {e}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.BLACK}{Back.YELLOW}Unknown error. Details: {e}{Style.RESET_ALL}")
            input()
        return t_list

def remove_from_list(t_list):
    """Handle instances of the user removing from the list"""

    removal_loop = True
    while removal_loop:
        view_list(t_list)
        print(f"{Fore.YELLOW}Enter the key of the item would you like to remove",
            f"{Fore.RED}Enter Q to end\n{Fore.RESET}")

        removal_input = input()

        if removal_input.lower() == "q":
            removal_loop = False
        else:
            try:
                del t_list[removal_input]
                return t_list
            except KeyError as e:
                print(f"Key error: {e}")
                input()
            except Exception:
                print(f"Unknown error. Details: {e}")
                input()

def view_list(t_list, massprint=True):
    """Handle Viewing the Task List"""

    if massprint:
        for item in t_list:
            print(f"{Fore.YELLOW}{item}:{Fore.MAGENTA} {t_list[item]}")
    else:
        print(f"{Fore.YELLOW}massprint disabled. Press enter to view each task")
        for item in t_list:
            print(f"{Fore.RED}{item}:{Fore.MAGENTA} {t_list[item]}{Fore.RESET}")
            input()
    input("press enter\n") # Freezes the screen until user presses enter

def cli(task_list):
    """The Command line instance of the Task List"""

    cli_loop = True
    version = "Test Version rel 3.\nPRIVATE ACCESS"
    
    print(Fore.YELLOW + version)

    while cli_loop:
        print('\033c') # Clear the console
        print(f"{Fore.BLUE}Select an operation to do to the task list{Fore.RED}")
        cli_choice = input(f"(V)iew | (A)dd | (R)emove | (S)ave | (L)oad | (Q)uit\n{Fore.RESET}")

        if cli_choice.lower() == "v":
            view_list(task_list)
        elif cli_choice.lower() == "a":
            task_list = add_to_list(task_list)
        elif cli_choice.lower() == "r":
            task_list = remove_from_list(task_list)
        elif cli_choice.lower() == "s":
            save_json(task_list)
        elif cli_choice.lower() == "l":
            task_list = load_json()
        elif cli_choice.lower() == "q":
            cli_loop = False
        else:
            print(f"{Back.YELLOW}{Fore.BLACK}'{cli_choice}' is not a valid input{Style.RESET_ALL}")
        

def main():
    """Handle the Selection of GUI or CLI. 
    This shuld currently only open CLI, as GUI does not exist"""

    task_list = load_json()
    cli(task_list) # TODO Once CLI, make this choose based on user settings. 


if __name__ == "__main__":
    init() # Initialize colorama
    main()

