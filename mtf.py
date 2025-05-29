def move_to_front(config, sequence):
    logs = []
    total_cost = 0
    for s in sequence:
        index = config.index(s)
        cost = index + 1
        total_cost += cost
        logs.append((config[:], s, cost))
        config.insert(0, config.pop(index))
    return total_cost, logs

def improved_mtf(config, sequence):
    logs = []
    total_cost = 0
    for i, s in enumerate(sequence):
        index = config.index(s)
        cost = index + 1
        total_cost += cost

        # Mayor diferencia entre los algoritmos. Ve si es que se usa el elemento nuevamente
        # si no se usa pronto, no lo mueve al frente
        lookahead = sequence[i+1:i+index]
        if s in lookahead:
            config.insert(0, config.pop(index))

        logs.append((config[:], s, cost))
    return total_cost, logs
