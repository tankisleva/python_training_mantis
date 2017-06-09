import random
import string
from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    if len(app.project.get_project_list()) == 0:
        name = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8))
        project = Project(name)
        app.project.create(project)
    old_projects = app.project.get_project_list()
    app.project.delete_project_by_name(old_projects[0])
    new_projects = app.project.get_project_list()
    assert len(new_projects) == len(old_projects) - 1