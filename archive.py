class Archive:
    def __init__(self,name_archive) :
        self.name_archive=name_archive
    def create(self):
        print(f"Creando archivo {self.name_archive}")
    def list(self):
        print("Listando archivos")
    def deleate(self):
        print(f"Eliminando archivo {self.name_archive}")
        