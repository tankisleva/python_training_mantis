from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href*='manage_overview_page.php']").click()
        if len(wd.find_elements_by_name("password")) != 0:
            wd.find_element_by_name("password").send_keys("root")
            wd.find_element_by_css_selector('input[type="submit"]').click()
        wd.find_element_by_css_selector("a[href*='manage_proj_page.php']").click()


    def submit_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    def create(self, new_project_data):
        self.open_manage()
        self.init_project_creation()
        self.fill_project_form(new_project_data)
        self.submit_project_creation()
        self.group_cache = None

    def init_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def delete_project_by_name(self, project):
        wd = self.app.wd
        self.open_manage()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        self.group_cache = None

    def type(self, filed_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(filed_name).click()
            wd.find_element_by_name(filed_name).clear()
            wd.find_element_by_name(filed_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.type("name", project.name)
        # self.type("description", project.description)
        # select = Select(wd.find_element_by_name('status'))
        # select.select_by_visible_text(project.status)

    group_cache = None

    def get_project_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_manage()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("tr a[href*='manage_proj_edit_page.php?project_id']"):
                text = element.text
                self.group_cache.append(Project(name=text))
        return list(self.group_cache)

