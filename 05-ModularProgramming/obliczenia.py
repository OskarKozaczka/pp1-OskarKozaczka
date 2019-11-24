import statistics


def srednia(kwoty):
    return statistics.mean(kwoty)
    
    
def mediana(kwoty):
    return statistics.median(kwoty)

def minimum(kwoty):
    return min(kwoty)

def maximum(kwoty):
    return max(kwoty)