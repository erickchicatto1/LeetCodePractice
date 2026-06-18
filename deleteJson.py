import pathlib

def eliminar_auth_json():
    # Obtiene la ruta del archivo "auth.json" en el directorio actual de ejecución
    archivo = pathlib.Path("auth.json")
    
    if archivo.exists():
        archivo.unlink()
        print("✅ El archivo auth.json fue eliminado exitosamente.")
    else:
        print("ℹ️ El archivo auth.json no existe en este directorio.")

if __name__ == "__main__":
    eliminar_auth_json()
