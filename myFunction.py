def myFunction(a: int):
    multiplicator: range = range(1,11)
    multiplicationTable = []
    for r in multiplicator:
        myString = "{r} * {a} = {result}".format(r = r, a = a, result = r * a)
        multiplicationTable.append(myString)
        if r != len(multiplicator):
            multiplicationTable.append("\n")
    result: str = ''.join(multiplicationTable)
    return result

# BEST ALTERNATIVE
def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))