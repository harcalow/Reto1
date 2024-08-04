import os

class Archive:
    def __init__(self,name_archive,text_archive) :
        self.name_archive=name_archive
        self.text_archive=text_archive
    def create(self):
        #print(f"Creando archivo {self.name_archive}")
        os.system(f"./bash.sh {self.name_archive} 1 '{self.text_archive}'")
    def list(self):
        os.system(f"./bash.sh {self.name_archive} 2")
    def deleate(self):
        os.system(f"./bash.sh {self.name_archive} 3")