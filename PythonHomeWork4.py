# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('33_Polynomial.txt', 'w') as data:
#     data.write(polynom1)

###############################################################################

# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('poly_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()


# with open('poly_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()

# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')