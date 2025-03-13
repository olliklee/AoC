from datetime import datetime
import pickle
from os import path


class Projects:
    id = 0
    FILE_NAME = "projects.pkl"

    def __init__(self):
        if path.exists(self.FILE_NAME):
            loaded = self.load()
            if isinstance(loaded, Projects):  # Sicherstellen, dass es ein Projects-Objekt ist
                self.projects = loaded.projects
                self.id = loaded.id
            else:
                print("⚠ Fehler: Ungültige Daten in projects.pkl – Erstelle neue Projekte-Liste.")
                self.projects = {}
                self.id = 0
                self.save()
        else:
            self.projects = {}
            self.id = 0
            self.save()

    def __str__(self):
        return '\n'.join([f'{project_id:3} {proj.name}' for project_id, proj in self.projects.items()])

    def add_project(self, name):
        self.id += 1
        new_project = Project(name=name)
        new_project.id = self.id
        self.projects[self.id] = new_project
        self.save()

    def get_project(self, id):
        return self.projects.get(id)

    def save(self):
        """Speichert die Projekte in einer Datei."""
        with open(self.FILE_NAME, 'wb') as file:
            pickle.dump(self, file, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):
        """Lädt die Projekte aus einer Datei, falls möglich."""
        try:
            with open(self.FILE_NAME, 'rb') as file:
                loaded_data = pickle.load(file)
                if isinstance(loaded_data, Projects):
                    return loaded_data
                else:
                    raise ValueError("Falsches Datenformat")
        except (FileNotFoundError, EOFError, ValueError, pickle.UnpicklingError):
            print("⚠ Fehler beim Laden – Erstelle neue Projekte-Liste.")
            return Projects()


class Project:
    def __init__(self, name):
        self.id = 0
        self.name = name
        self.short = 'New Project'
        self.long = None
        self.owner = None
        self.collaborators = []
        self.published = datetime.now()
        self.notes = []
        self.tasks = []
        self.todos = []

    def __str__(self):
        return f'{self.id}: {self.name} - "{self.short}" by {self.owner}'

    def add_note(self, text):
        self.notes.append(Note(text))

    def add_task(self):
        self.tasks.append(Task(name='New Task'))

    def add_todo(self):
        self.todos.append(Todo(name='New ToDo'))

    def full_info(self):
        return f'''
{self.id}: {self.name} by {self.owner}
   {self.short}
   {self.long}
   Notes:         {', '.join([n.name for n in self.notes])}
   Collaborators: {', '.join([c for c in self.collaborators])}
   Tasks:         {', '.join([ta.name for ta in self.tasks])}
   ToDos:         {', '.join([to.name for to in self.todos])}
'''


class Note:
    def __init__(self, name):
        self.added = datetime.now()
        self.name = name

    def __str__(self):
        return f'{self.added:%D} {self.name}'

    def __repr__(self):
        return f'{self.added:%D} {self.name}'


class Detail:
    def __init__(self, name):
        self.added = datetime.now()
        self.name = name
        self.notes = []

    def __str__(self):
        return f'{self.added:%D} {self.name}'

    def __repr__(self):
        return f'{self.added:%D} {self.name}'

    def add_note(self, text):
        self.notes.append(Note(text))


class Task(Detail):
    def __init__(self, name, start=None, end=None,
                 confirmation_date=None, ressource=None,
                 assigned=None, assigned_confirmed=None):
        super().__init__(name)
        self.start = start
        self.end = end
        self.confirmation_date = confirmation_date
        self.ressource = ressource
        self.assigned = assigned
        self.assigned_confirmed = assigned_confirmed

    def __repr__(self):
        return f'{self.added} {self.name}  {len(self.notes)}'


class Todo(Detail):
    def __init__(self, name, due=None, who=None, status='Unfinished'):
        super().__init__(name)
        self.due = due
        self.who = who
        self.status = status

    def __repr__(self):
        return f'{self.added} {self.name} Status: {self.status} Notes: {len(self.notes)}\n'
