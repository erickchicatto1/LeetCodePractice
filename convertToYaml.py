import yaml
import os

def crear_configuracion_yolo(ruta_raiz):
    path_classes = os.path.join(ruta_raiz, 'classes.txt')
    path_yaml = os.path.join(ruta_raiz, 'data.yaml')

    # 1. Leer nombres de clases
    if not os.path.exists(path_classes):
        print("Error: No se encontró classes.txt")
        return

    with open(path_classes, 'r') as f:
        classes = [line.strip() for line in f.readlines() if line.strip()]

    # 2. Crear diccionario de datos
    # Usamos la misma carpeta para train y val si no tienes un split hecho
    data = {
        'path': ruta_raiz, 
        'train': 'images', 
        'val': 'images',   
        'nc': len(classes),
        'names': classes
    }

    # 3. Guardar archivo YAML
    with open(path_yaml, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    
    print(f"Archivo data.yaml creado en: {path_yaml}")
    return path_yaml

# EJECUCIÓN
mi_ruta = "D://UpgradeKnowC_Python//PythonUpgrade//project-3" # CAMBIA ESTO por tu ruta real
crear_configuracion_yolo(mi_ruta)
