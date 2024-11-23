import itertools
from datetime import datetime as dt

DATE_TIME_FORMAT = "%d/%m/%Y %H:%M:%S"


class Note:
    id_iter = itertools.count()

    def __init__(self, note_title, note_text, note_id, note_datetime):
        if note_id:
            self.__id = note_id
            Note.id_iter = itertools.count(note_id + 1)
        else:
            self.__id = next(self.id_iter)
        self.title = note_title
        self.text = note_text
        if note_datetime:
            print(note_datetime)
            self.__date_time = dt.strptime(note_datetime, DATE_TIME_FORMAT).strftime(DATE_TIME_FORMAT)
        else:
            self.__date_time = dt.now().strftime(DATE_TIME_FORMAT)

    @property
    def date_time(self):
        return self.__date_time

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    def __str__(self):
        return "{:<3} {:<30} {:<20}".format(self.__id, self.title, self.date_time)

    def print_note(self):
        print(f"Id - {self.__id}")
        print(f"Title - {self.__title}")
        print(f"Text \n{self.__text}")

    def edit(self, title, text):
        self.title = title
        self.text = text
        self.__date_time = dt.now().strftime(DATE_TIME_FORMAT)
