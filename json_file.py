import json
import os

FILE_NAME = "db.json"


class JsonFile:

    @staticmethod
    def save(note_list):
        with open(FILE_NAME, "w") as f:
            json.dump([note.__dict__ for note in note_list], f, indent=2)

    @staticmethod
    def load():
        if os.path.isfile(FILE_NAME) and os.access(FILE_NAME, os.R_OK):
            # checks if file exists
            # print("File exists and is readable")
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        else:
            return []
