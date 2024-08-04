import os
from archive import Archive
def main():
    option=0
    os.system("chmod +x bash.sh")
    while(option not in range(1, 5)):
        print("""Bienvenido ¿Que deseas hacer?
            1) Crear un archivo  
            2) Listar archivos  
            3) Eliminar un archivo 
            4) Salir 
    
            """)
        try:
            option = int(input("Ingresa el número de la opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    match option:
        case 1:
            name_archive = input("Opción 1 Crear un archivo \n Ingrese el nombre con extensión del archivo a crear: \n ->")
            text_archive = input("Ingrese contenido del archivo: \n ->")
            archive_one=Archive(name_archive,text_archive)
            archive_one.create()
        case 2:
            print("Opción 2 Listar archivos:")
            archive_one=Archive("null")
            archive_one.list()
        case 3:
            name_archive = input("Opción 3 Eliminar un archivo \n Ingrese el nombre con extensión del archivo a eliminar: \n ->")
            archive_one=Archive(name_archive)
            archive_one.deleate()
        case _:
            print("Opción 4 salir Vuelva pronto")


if __name__ == "__main__":
    main()