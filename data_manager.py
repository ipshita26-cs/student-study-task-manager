import json
import os


DATA_FOLDER = "data"


def load_data(filename):
    """Load data from a JSON file."""

    file_path = os.path.join(DATA_FOLDER, filename)

    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(filename, data):
    """Save data to a JSON file."""

    file_path = os.path.join(DATA_FOLDER, filename)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)