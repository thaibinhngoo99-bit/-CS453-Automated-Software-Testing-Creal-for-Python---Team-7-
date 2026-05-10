def is_near(val, expected, tolerance=0.001):
    if val > expected + tolerance:
        return False
    if val < expected - tolerance:
        return False
    return True