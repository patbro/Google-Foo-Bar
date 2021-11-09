def solution(xs):
    if not isinstance(xs, list):
        return

    if len(xs) == 1 and xs[0] < 0:
        return str(xs[0])

    sanitized_positives = []
    sanitized_negatives = []
    for i in xs:
        if (i > 0) and abs(i) <= 1000:
           sanitized_positives.append(i)
        elif (i < 0) and abs(i) <= 1000:
            sanitized_negatives.append(i)
    
    if (len(sanitized_negatives) % 2) != 0:
        sanitized_negatives.sort()
        sanitized_negatives.pop()

    if (sanitized_positives) or (sanitized_negatives):
        product_positives = list_product(sanitized_positives)
        product_negatives = list_product(sanitized_negatives)

        products = product_positives * product_negatives
        return str(int(products))

    return str(0)

def list_product(input_list):
    product = 1
    for i in input_list:
        product = product * i

    return product

print(solution([]))
print(solution([-1]))
print(solution([-1, -1, -1]))
print(solution([-2, -2]))
print(solution([0, 0, -4]))
print(solution([2, -3, 1, 0, -5]))
print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([1000000, -4, 4]))
print(solution([696, 254, 707, 730, 252, 144, 18, -678, 921, 681, -665, 421, -501, 204, 742, -609, 672, -72, 339, -555, -736, 230, -450, 375, 941, 50, 897, -192, -912, -915, 609, 100, -933, 458, -893, 932, -590, -209, 107, 473, -311, 73, 68, -229, 480, 41, -235, 558, -615, -289, -643]))
