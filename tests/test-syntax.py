import os 

def test():
    # Compilación del código para checkear la sintaxis.( Compilamos todos los archivos que se encuentran en src)
    return os.system("python -m compileall src")
    