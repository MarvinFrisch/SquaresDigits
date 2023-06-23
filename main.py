import math

def permutations(list):
    if len(list) <=1:
        yield list
    else:
        for perm in permutations(list[1:]):
            for i in range(len(list)):
                yield perm[:i]+list[0:1]+perm[i:]

def intToBase(number, base):
    list = []
    for i in range(1, 100000):
        list.append(str(number % (base)))
        number = int(number/base)
        if number == 0:
            break
    list.reverse()
    return list

def calculate(operator, left, right):
    result = 'Error'
    if operator == '+':
        result = left+right
    if operator == '-':
        result = left-right
    if operator == '*':
        result = left*right
    if operator == '/':
        if right != 0:
            result = left/right
    if operator == '^':
        result = left**right
    if operator == '!':
        result = math.factorial(left)

    return result

operators = ["+", "-", "*", "/", '^']

operator_importance = [['!'], ['^'], ["*", "/"], ["+", "-"]]
operator_singles = []

max = 1000

for number in range(max+1):
    root = math.sqrt(number)
    number = str(number)
    digits = [*number]
    for digits_reordered in permutations(digits):
        for i in range(len(operators)**len(number)):
            operator_order = intToBase(i, len(number))
            while len(operator_order) < len(operators):
                operator_order.insert(0, '0')
            operator_order_no_zeroes = [i for i in operator_order if i != '0']
            if len(operator_order_no_zeroes) == len(set(operator_order_no_zeroes)):
                formula = ''
                for index_formula in range(len(number)):
                    if index_formula >= 1 and str(index_formula) in operator_order:
                        formula += operators[operator_order.index(str(index_formula))]
                    formula += digits_reordered[index_formula]
                    if len(formula) > len(number):
                        formula2 = formula
                        operators_in_formula = []
                        for symbol in formula2:
                            if symbol in operators:
                                operators_in_formula.append(symbol)
                        for operator in operators:
                            formula2 = formula2.replace(operator, ',')
                        formula_split = formula2.split(',')
                        formula_split = [float(i) for i in formula_split]
                        operators_in_formula2 = operators_in_formula.copy()
                        for importance_group in operator_importance:
                            for operator in operators_in_formula:
                                if operator in importance_group:
                                    result = calculate(operator, formula_split[operators_in_formula2.index(operator)], formula_split[operators_in_formula2.index(operator)+1])
                                    if result != 'Error':
                                        formula_split[operators_in_formula2.index(operator)] = result
                                        if operator not in operator_singles:
                                            formula_split.pop(operators_in_formula2.index(operator)+1)
                                    operators_in_formula2.remove(operator)
                        if len(formula_split) == 1:
                            if root == formula_split[0]:
                                print(f"Number: {number} possible! {formula} = {formula_split[0]}")

