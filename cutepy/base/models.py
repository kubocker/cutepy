import os


class BaseModel(object):
    """ class Table
    @param
    """
    name = ""

    def __init__(self, *args):
        self.file_path = "{file_path}/{name}.json".format(file_path="", name=self.name)

    def add(self):
        pass

    def remove(self, id):
        pass

    def update(self, id):
        pass

    def list(self, id):
        pass

    def all(self):
        pass

    def post(self):
        pass
