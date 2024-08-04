#!/bin/bash
option=$2
if [ "$2" = "1" ]; then 
    echo "Creando archivo $1"
    touch $1
    echo "$3" > $1
elif [ "$2" = "2" ]; then
    echo "Listando archivos"
    ls 
else
    if [ -e "$1" ]; then
        rm "$1"
        echo "Archivo $1 eliminado exitosamente."
    else
        echo "Error: El archivo $1 no existe."
    fi
fi