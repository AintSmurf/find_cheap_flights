import os


class System_helper:
    def __init__(self) -> None:
        self.system_helper = os

    def delete_file(self):
        self.system_helper.remove("urls.csv")
