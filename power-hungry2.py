def solution(xs):
    negatives = [num for num in xs if num < 0]
    positives = [num for num in xs if num > 0]

    if len(negatives) % 2 != 0:
        negatives.sort()
        negatives.pop()

    if positives or negatives:
        product = 1
        for x in positives + negatives:
            product *= x

        return str(product)

    return '0'

print(solution([0, 0, -4]))
print(solution([2, -3, 1, 0, -5]))
print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([1000000, -4, 4]))
