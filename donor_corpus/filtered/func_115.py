def exception_distance(a):
    distance = 0
    while a.FullName != 'System.Exception':
        a = a.BaseType
        distance += 1
    return distance