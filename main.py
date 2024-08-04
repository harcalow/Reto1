from archive import Archive

def main():
    option=0
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
        

    

if __name__ == "__main__":
    main()
