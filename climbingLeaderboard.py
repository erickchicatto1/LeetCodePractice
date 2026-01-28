def createRank(scores):
    # Esta función crea la lista de posiciones (1, 2, 2, 3...)
    rank = []
    currScore = scores[0]
    count = 1
    
    for score in scores:
        if score != currScore:
            currScore = score
            count += 1
        rank.append(count)
        
    return rank

def climbingLeaderboard(ranked, player):
    # 1. Creamos el mapa de rangos
    rank = createRank(ranked)
    
    # 2. Agregamos los "centinelas" al final para no salirnos del índice
    ranked.append(-1)
    rank.append(rank[-1] + 1)
    
    res = []
    
    # Puntero iniciando al final de la lista (los puntajes más bajos)
    pointer = len(ranked) - 1
    
    print("\n--- INICIO DEL DEBUG ---")
    print(f"Tablero inicial: {ranked}")
    print(f"Rangos calculados: {rank}")
    print("-" * 30)

    for playerScore in player:
        print(f"\nJugando con puntaje: {playerScore}")
        
        while pointer >= -1:
            if pointer - 1 >= 0:
                # Este print te dirá qué está comparando en cada momento
                # Muestra: Tu Puntaje | Puntaje en la tabla | Rango en esa posición
                print(f"   Comparando: {playerScore} vs {ranked[pointer-1]} (Rango: {rank[pointer-1]})")
                
                if playerScore > ranked[pointer-1]:
                    print("   -> ¡Soy mejor! Subo un escalón (pointer -= 1)")
                    pointer -= 1
                elif playerScore == ranked[pointer-1]:
                    print(f"   -> ¡Empate! Me quedo con el rango {rank[pointer-1]}")
                    res.append(rank[pointer-1])
                    break
                else:
                    # Aquí decidimos si nos quedamos en el escalón actual o el siguiente
                    if playerScore >= ranked[pointer]:
                        print(f"   -> No supero al de arriba, pero gano/empato al actual. Rango: {rank[pointer]}")
                        res.append(rank[pointer])
                        break
                    else:
                        print(f"   -> Soy peor que el actual. Me toca el siguiente rango: {rank[pointer]+1}")
                        res.append(rank[pointer]+1)
                        break
            else:
                # Caso extremo (principio de la lista)
                if playerScore >= ranked[pointer]:
                    res.append(rank[pointer])
                    break
                else:
                    res.append(rank[pointer]+1)
                    break
                        
    return res

# --- AQUÍ EMPIEZA EL MAIN ---
if __name__ == "__main__":
    # DATOS DE PRUEBA
    # El tablero de líderes actual (de mayor a menor)
    ranked_scores = [100, 90, 90, 80]
    
    # Tus puntajes en los juegos (de menor a mayor)
    player_scores = [70, 80, 105]

    print(f"Input Ranked: {ranked_scores}")
    print(f"Input Player: {player_scores}")

    # Llamamos a la función
    resultado = climbingLeaderboard(ranked_scores, player_scores)

    print("\n" + "="*30)
    print(f"RESULTADO FINAL: {resultado}")
    print("="*30)