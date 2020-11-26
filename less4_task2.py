import cProfile
import timeit

N1 = 100
N2 = 200
N3 = 400
N4 = 800
N5 = 1600


def use_sieve_algo(number):
    n = 10
    result_li = []
    while len(result_li) < number:
        sieve = [i for i in range(n)]
        sieve[1] = 0
        for i in range(2, n):
            if sieve[i] != 0:
                if len(result_li) <= i - 2 or sieve[i] != result_li[i - 2]:
                    result_li.append(sieve[i])
                j = i + i
                while j < n:
                    sieve[j] = 0
                    j += i
        n *= 10
    return result_li[number - 1]


print(timeit.timeit('use_sieve_algo(N1)', number=100, globals=globals()))  # 0.0646175
print(timeit.timeit('use_sieve_algo(N2)', number=100, globals=globals()))  # 0.7325069
print(timeit.timeit('use_sieve_algo(N3)', number=100, globals=globals()))  # 0.9450621000000001
print(timeit.timeit('use_sieve_algo(N4)', number=100, globals=globals()))  # 1.3184030999999998
print(timeit.timeit('use_sieve_algo(N5)', number=100, globals=globals()))  # 9.4671616

cProfile.run('use_sieve_algo(N5)')


# 1    0.064    0.064    0.073    0.073 less4_task2.py:11(use_sieve_algo)
# 5    0.005    0.001    0.005    0.001 less4_task2.py:15(<listcomp>)

def non_use_sieve(number):
    simple_lis = [2]
    complex_li = [2]
    while len(simple_lis) - 1 != number:

        complex_li.append(complex_li[-1] + 1)
        assist = 0

        for i in complex_li[:-1]:
            if complex_li[-1] % i != 0:
                assist += 1

        if assist == len(complex_li) - 1:
            simple_lis.append(complex_li[-1])

    return simple_lis[-1]


print(timeit.timeit('non_use_sieve(N1)', number=1, globals=globals()))  # 0.022849199999999993
print(timeit.timeit('non_use_sieve(N2)', number=1, globals=globals()))  # 0.1245992
print(timeit.timeit('non_use_sieve(N3)', number=1, globals=globals()))  # 1.0095352
print(timeit.timeit('non_use_sieve(N4)', number=1, globals=globals()))  # 4.1539187
print(timeit.timeit('non_use_sieve(N5)', number=1, globals=globals()))  # 19.7879933

cProfile.run('non_use_sieve(N3)')

#  1    0.599    0.599    0.601    0.601 less4_task2.py:41(non_use_sieve)


'''
    Второй алгоритм по понятным причинам работает в разы дольше, имеет приюлизительно квадратичную 
    сложность.
    У первого варианта крайне сложно по имеющимся данным отследить сложность, так как соседние
    показания могу отличаться в 9 раз, а могут быть очень близки.
'''