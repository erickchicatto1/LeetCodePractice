def ConnectFourWinner(strArr):
    # 1. Identificar al jugador actual
    player = strArr[0]
    
    # 2. Limpiar el tablero: quitamos (), espacios y dividimos por coma
    board = []
    for row_str in strArr[1:]:
        # Reemplazamos paréntesis y espacios antes de hacer el split
        clean_row = row_str.replace("(", "").replace(")", "").replace(" ", "").split(",")
        board.append(clean_row)
    
    rows = 6
    cols = 7

    def check_win(r, c, p):
        # Direcciones: Horizontal, Vertical, Diagonal \, Diagonal /
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            # Revisar en ambas direcciones (adelante y atrás)
            for direction in [1, -1]:
                step = 1
                while True:
                    nr = r + (dr * step * direction)
                    nc = c + (dc * step * direction)
                    # Verificamos límites y si la ficha es del mismo jugador
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == p:
                        count += 1
                        step += 1
                    else:
                        break
            if count >= 4:
                return True
        return False

    # 3. Probar cada columna de izquierda a derecha
    for c in range(cols):
        # Reiniciamos target_row para cada columna para evitar el error de referencia
        target_row = -1
        
        # 4. Gravedad: Buscar la fila más baja disponible ('x')
        for r in range(rows - 1, -1, -1):
            if board[r][c] == 'x':
                target_row = r
                break
        
        # 5. Si la columna no está llena, simulamos el tiro
        if target_row != -1:
            board[target_row][c] = player # Ponemos la ficha
            
            if check_win(target_row, c, player):
                # Formato exacto requerido: (Fila x Columna)
                # Usamos concatenación simple para evitar errores de f-strings
                return "(" + str(target_row + 1) + "x" + str(c + 1) + ")"
            
            # ¡IMPORTANTE! Si no ganó, hay que quitar la ficha para la siguiente prueba
            board[target_row][c] = 'x'

    return "none"