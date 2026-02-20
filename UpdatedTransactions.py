def transactionOperations(transactions):
    totals = {}  # diccionario para acumular montos por usuario

    for _, user, amount in transactions:
        print(f"{_} {user} {amount}")

        # Verificar si la clave existe
        if user in totals:
            totals[user] += amount
        else:
            totals[user] = amount  # inicializamos si no existía

    # Retornar como lista de tuplas (usuario, total)
    result = [(user, total) for user, total in totals.items()]

    return result


if __name__ == "__main__":
    transactions = [
        (1, "user1", 150),
        (2, "user3", 100),
        (3, "user2", 150),
        (4, "user1", 200),
        (2, "user2", 100)
    ]

    totals_list = transactionOperations(transactions)
    print(totals_list)
