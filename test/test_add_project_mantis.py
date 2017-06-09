import random
import string
from model.project import Project


def test_add_project(app):
    name = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8))
    project = Project(name)
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(new_projects) == len(old_projects) + 1
    old_projects.append(project)
    assert sorted(old_projects, key=Project.sort_by_alphabet) == sorted(new_projects, key=Project.sort_by_alphabet)