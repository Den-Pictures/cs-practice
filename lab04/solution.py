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

def ranking(names, scores):
    participants = []
    for i in range(len(names)):
        participants.append((names[i], scores[i], i))
    participants.sort(key=lambda x: (-x, x))
    result_names =[]
    for i in participants:
        result_names.append(i)
    return result_names

def above_average(names, scores):
    avg = average(scores)
    above_avg_list = []
    for i in range(len(names)):
        if scores[i] > avg:
            above_avg_list.append(names[i])
    return above_avg_list