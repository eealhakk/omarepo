from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        print("get projekt alkaa")
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        data = toml.loads(content)
        #print("\nTOML muutettuna Python dataksi:")
        #print(data)

        tool = data["tool"]["poetry"]

        name = tool.get("name")
        description = tool.get("description")

        dependencies = list(tool.get("dependencies", {}).keys())
        dev_dependencies = list(tool.get("group", {}).get("dev", {}).get("dependencies", {}).keys())


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
        #print("Project")
        #print(Project(name, description, dependencies, dev_dependencies))
        return Project(name, description, dependencies, dev_dependencies)
