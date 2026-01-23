import requests

def count_ages():
    url = "https://coderbyte.com/api/challenges/json/age-counting"
    response = requests.get(url)
    
    # 1. Obtenemos el string de la llave 'data'
    data_string = response.json()['data']
    
    # 2. Separamos por comas para obtener cada par (key=xxx o age=xxx)
    # Ejemplo: ["key=iafpk", "age=58", "key=wnvi ", "age=64"]
    items = data_string.split(',')
    
    count = 0
    for item in items:
        # 3. .strip() elimina espacios invisibles al inicio y final
        # .replace(" ", "") elimina espacios en medio como "age = 50"
        clean_item = item.strip().replace(" ", "")
        
        # 4. Verificamos si la parte limpia empieza con 'age='
        if clean_item.startswith('age='):
            # 5. Extraemos el valor después del '='
            age_value = int(clean_item.split('=')[1])
            
            if age_value >= 50:
                count += 1
                
    # 6. Imprimimos SOLO el número final
    print(count)

if __name__ == "__main__":
    count_ages()