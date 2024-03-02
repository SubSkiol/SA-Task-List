"""Load, save, and manage tasks inside of a task list.
This base should be used for both CLI and GUI varients of the Task List."""
import json



# Start json section 
def load_json():
    """Load data from the JSON file."""

    try:
        with open("list_data.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print("No existing data file found.")
        return dict()

def save_json(data):
    """Save current instance of the task list. 
    This should print the list then ask for confirmation before overwriting the JSON."""

    print(data, "Are you sure you wish to save? This will overwrite the file.")
    save_confirmation = input("Enter Y to agree: ").lower()

    if save_confirmation == "y":
        with open("list_data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2)


def add_to_list(t_list):
    """Handle instances of adding to the task list"""

    add_loop = True
    while add_loop:
        print("Enter a unique name (key) for your task",
              "Warning: If the key already exists, data will be overwritten.")
        user_key = input("Press Q to quit")
        if user_key.lower() == "q":
            add_loop = False

        print(f"Task name is '{user_key}'")

        user_value = input("Type the task\n")

        try:
            t_list[user_key] = user_value
            print(f"Added task!",
                  {t_list[user_key]})
            add_loop = False
        except ValueError as e:
            print(f"Value error: {e}")
        except SyntaxError as e:
            print(f"Syntax error: {e}")
        except KeyError as e:
            print(f"Key error: {e}")
        except Exception as e:
            print(f"Unknown error. Details: {e}")
    return t_list

def remove_from_list(t_list):
    """Handle instances of the user removing from the list"""

    removal_loop = True
    while removal_loop:
        print(t_list, "Enter the key of the item would you like to remove.",
            "Enter Q to end")

        removal_input = input()

        if removal_input.lower() == "q":
            removal_loop = False
        else:
            try:
                del t_list[removal_input]
                return t_list
            except ValueError as e:
                print(f"Value error: {e}")
            except SyntaxError as e:
                print(f"Syntax error: {e}")
            except KeyError as e:
                print(f"Key error: {e}")
            except Exception:
                print(f"Unknown error. Details: {e}")  

def cli(task_list):
    """The Commandline Instance of the Task List"""

    cli_loop = True
    print("Test Version")

    while cli_loop:
        print("Select an operation to do to the task list")
        cli_choice = input("(V)iew | (A)dd | (R)emove | (S)ave | (L)oad | (Q)uit\n")

        if cli_choice.lower() == "v":
            print(task_list)
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
            print(f"'{cli_choice}' is not a valid input")
        

def main():
    """Handle the Selection of GUI or CLI. 
    This shuld currently only open CLI, as GUI does not exist"""

    task_list = load_json()
    cli(task_list) # TODO Once CLI, make this choose based on user settings. 


if __name__ == "__main__":
    main()
