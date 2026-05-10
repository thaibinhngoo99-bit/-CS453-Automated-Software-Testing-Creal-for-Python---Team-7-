def solve_problem():
    total_letters = 0
    for n in range(1, 1001):
        total_letters += len(build_words(n))
    return total_letters