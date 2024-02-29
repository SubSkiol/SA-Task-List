"""Load, save, and manage tasks inside of a task list.
This base should be used for both CLI and GUI varients of the Task List."""
import json

task_list = dict() # Create an empty dictionary that we can add to later

# Start json section 
def load_json():
    """Load data from the JSON file."""

    try:
        with open("list_data.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print("No existing data file found.")
        return None

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
        user_key = input()
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
        except Exception:
            print(f"Unknown error. Details: {e}")
    return t_list

def remove_from_list(t_list):
    """Handle instances of the user removing from the list"""

    removal_loop = True
    while removal_loop:
        print(t_list, "Enter the key of the item would you like to remove.",
            "Enter Q to end")

        removal_input = input()
        try:
            del t_list[removal_input]
        except ValueError as e:
            print(f"Value error: {e}")
        except SyntaxError as e:
            print(f"Syntax error: {e}")
        except KeyError as e:
            print(f"Key error: {e}")
        except Exception:
            print(f"Unknown error. Details: {e}")

        return t_list    

def cli():
    """The Commandline Instance of the Task List"""

def main():
    """Handle the Selection of GUI or CLI. 
    This shuld currently only open CLI, as GUI does not exist"""

if __name__ == "__main__":
    main()
