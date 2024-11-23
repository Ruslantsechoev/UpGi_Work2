from json_file import JsonFile
from note import Note


def delete(note):
    note_list.remove(note)


def add(note_title, note_text, note_id=None, note_datetime=None):
    note_list.append(Note(note_title, note_text, note_id, note_datetime))


def edit(note: Note):
    title = input("Введите заголовок:\n")
    text = input("Введите текст:\n")
    note.edit(title, text)


def choose_note(note_id):
    match = None
    for note in note_list:
        if note.id == note_id:
            match = note
            break
    if match:
        match.print_note()
        com = input("Вы можете удалить или редактировать эту записку(edit, delete)\n")
        match com:
            case "edit":
                edit(match)
            case "delete":
                delete(match)
    else:
        print(f"Записка с id {note_id} не найдена")


def show_notes():
    if note_list:
        print("{:<3} {:<30} {:<20}".format("id", "title", "datetime"))
        for note in sorted(note_list, key=lambda x: x.date_time):
            print(note)
    else:
        print("Пока нету никаких записей")


def save():
    JsonFile.save(note_list)


def load():
    data = JsonFile.load()
    # print(data)
    for note in data:
        add(note['_Note__title'], note['_Note__text'], note['_Note__id'], note['_Note__date_time'])


note_list = []
load()
is_not_finished = True
while is_not_finished:
    show_notes()
    command = input("Введите команду(add, choose, save, exit):\n")
    match command:
        case "add":
            title = input("Введите заголовок:\n")
            text = input("Введите текст:\n")
            add(title, text)
        case "choose":
            note_id = int(input("Введите номер id\n") or "0")
            choose_note(note_id)
        case "save":
            save()
        case "exit":
            is_not_finished = False
        case _:
            print("Не верная команда")
