# Given an integer numRows, return the first numRows of Pascal's triangle.

def generate(num_rows):
    result = [[1], [1, 1]]
    a = []
    if num_rows == 1:
        return [[1]]
    if num_rows == 2:
        return result

    for i in range(1, num_rows-1):
        last_list = result[-1]
        a = [1, 1]
        for j in range(0, len(last_list) - 1):
            a.insert(j+1, last_list[j]+last_list[j+1])
        result.append(a)
    return result




