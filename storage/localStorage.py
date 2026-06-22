"""Persistence helpers for the CSV experiment data and JSON settings."""
import os
import json

import pandas

from config.dir import user_dir, history_dir, exam_dir, metadata_dir, keyboard_dir
from config.constant import USER_COLUMNS, HISTORY_COLUMNS


class CsvHandler:
    """Read/write helper around a single CSV data file."""

    def __init__(self, path):
        self.path = path

    def readData(self):
        return pandas.read_csv(self.path)

    def readStructure(self):
        return pandas.read_csv(self.path, nrows=1)

    def truncate(self):
        df = pandas.read_csv(self.path)
        df = pandas.DataFrame(columns=df.columns)
        df.to_csv(self.path, index=False)

    def append_data(self, new_df):
        df_csv = pandas.read_csv(self.path)
        result = pandas.concat([df_csv, new_df], ignore_index=True)
        result.to_csv(self.path, index=False)


class JsonHandler:
    """Read/write helper around a single JSON settings file."""

    def __init__(self, path):
        self.path = path

    def read_data(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return None

    def write_data(self, data):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def append_data(self, new_data):
        existing_data = self.read_data()
        if existing_data is None:
            existing_data = []
        existing_data.extend(new_data)
        self.write_data(existing_data)


class DataHandaler:
    """Facade over the experiment's CSV/JSON files used by the UI."""

    def __init__(self):
        # The participant-data files are runtime output (git-ignored); create
        # them with their canonical headers on first run so a fresh checkout works.
        self._ensure_seed_files()

        self.user_data_handaler = CsvHandler(path=user_dir)
        self.history_data_handaler = CsvHandler(path=history_dir)
        self.exam_data_handler = CsvHandler(path=exam_dir)
        self.metadata_handler = JsonHandler(path=metadata_dir)

    @staticmethod
    def _ensure_seed_files():
        for path, columns in ((user_dir, USER_COLUMNS), (history_dir, HISTORY_COLUMNS)):
            if not os.path.exists(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                pandas.DataFrame(columns=columns).to_csv(path, index=False)

    def get_new_sessionId(self):
        user_df = self.user_data_handaler.readData()
        if user_df.empty:
            return 1
        max_value = user_df['participantID'].max()
        return int(max_value) + 1

    def get_exam(self):
        return pandas.read_csv(exam_dir)

    def get_user(self):
        return self.user_data_handaler.readData()

    def append_history_data(self, new_df):
        self.history_data_handaler.append_data(new_df=new_df)

    def append_user_data(self, new_df):
        self.user_data_handaler.append_data(new_df=new_df)

    def readStructure_user(self):
        return self.user_data_handaler.readStructure()

    def resetHistory(self):
        self.user_data_handaler.truncate()
        self.history_data_handaler.truncate()

    def loadMetaData(self):
        return self.metadata_handler.read_data()

    def saveMetaData(self, data_dict):
        self.metadata_handler.write_data(data_dict)

    def getKeyboardList(self):
        setting_dict = self.metadata_handler.read_data()
        layout = CsvHandler(path=os.path.join(keyboard_dir, setting_dict['selected_keyboard_layout']))
        return layout.readData()['label'].to_list()

    def getSimilarities(self):
        setting_dict = self.metadata_handler.read_data()
        return list(range(1, int(setting_dict['selected_similarity']) + 1))


dataHandaler = DataHandaler()
