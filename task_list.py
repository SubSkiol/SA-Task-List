"""Load, save, and manage tasks inside of a task list.
This base should be used for both CLI and GUI varients of the Task List."""
# import json

task_list = dict() # Create an empty dictionary that we can add to later

def load_json():
    """Load existing Task Lists""" 

def save_json():
    """Save current istance of task list. 
    This should print the list then ask for confirmation before overwriting the json."""

def add_to_list():
    """Handle instances of adding to the task list"""

def remove_from_list():
    """Handle instances of the user removing from the list"""

def cli():
    """The Commandline Instance of the Task List"""

def main():
    """Handle the Selection of GUI or CLI. 
    This shuld currently only open CLI, as GUI does not exist"""

if __name__ == "__main__":
    main()
