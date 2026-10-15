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

def ranking(names: list[str], scores: list[float]) -> list[str]:
    participants = [(names[i], scores[i]) for i in range(len(names))]
    participants.sort(key=lambda x: -x[1])
    return [name for name, _, _ in participants]

def above_average(names, scores):
    avg = average(scores)
    above_avg_list = []
    for i in range(len(names)):
        if scores[i] > avg:
            above_avg_list.append(names[i])
    return above_avg_list