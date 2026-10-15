def average(scores):
    if len(scores) == 0:
        return 0.0
    total = sum(scores)
    count = len(scores)
    avg = total / count
    return round(avg, 2)

def winner(names, scores):
    best_index = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
    return names[best_index]

