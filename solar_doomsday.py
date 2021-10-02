def solution(area):
    solutions = []
    if area not in range(1, 1000000+1):
        return solutions

    recursive_solver(area, solutions)
    return solutions

def recursive_solver(area, solutions):
    power_2 = 1
    while(next_power_2(power_2) <= area):
        power_2 += 1

    solutions.append(power_2 ** 2)
    if power_2 ** 2 != area:
        recursive_solver(area - (power_2 ** 2), solutions)

def next_power_2(power_2):
    return (power_2+1) ** 2
