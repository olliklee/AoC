from classes import *


def main():
    akt = Projects()
    print(akt)
    # for _, project in akt.projects.items():
    #     print(project.full_info())
    p: Project = akt.get_project(1)
    print(p)
    p.short = "Short"
    p.long = "Long Description comes here"
    p.owner = "Rinser"
    p.collaborators = ["Rinser", "Hermannsländer"]
    p.add_note("First Note")
    p.add_task()
    p.tasks[0].add_note("Task Note")
    p.add_todo()
    p.add_todo()

    print(p.full_info())
    print(p.todos)
    if input('Save? (y/n): ') == 'y':
        akt.save()






if __name__ == '__main__':
    main()
