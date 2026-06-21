import json
import os

from content_item import TechnologyUpdate


class CMSManager:
    """
    Manages technology updates stored in a JSON file.
    """

    def __init__(self, filename="data.json"):
        self.filename = filename
        self.updates = []
        self.load_updates()

    def load_updates(self):
        """
        Load updates from the JSON file.
        If the file does not exist, start with an empty list.
        """
        if not os.path.exists(self.filename):
            self.updates = []
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.updates = [TechnologyUpdate.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.updates = []

    def save_updates(self):
        """
        Save all updates to the JSON file.
        """
        data = [update.to_dict() for update in self.updates]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def get_all_updates(self):
        """
        Return the list of all technology updates.
        """
        return self.updates

    def add_update(self, update):
        """
        Add a new technology update and save it.
        """
        self.updates.append(update)
        self.save_updates()

    def update_item(self, index, updated_update):
        """
        Replace an existing update at the given index.
        """
        if 0 <= index < len(self.updates):
            self.updates[index] = updated_update
            self.save_updates()

    def delete_update(self, index):
        """
        Delete an update at the given index.
        """
        if 0 <= index < len(self.updates):
            del self.updates[index]
            self.save_updates()