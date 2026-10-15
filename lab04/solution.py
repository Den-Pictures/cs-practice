def average(scores):
    if len(scores) == 0:
        return 0.0
    total = sum(scores)
    count = len(scores)
    avg = total / count
    return round(avg, 2)

