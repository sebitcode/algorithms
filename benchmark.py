from timeit import Timer

t = Timer("distance_v1('kitten', 'sitting')", "from levenshtein.levenshtein import distance_v1")
print(t.timeit(number=1))

t = Timer("distance_v2('kitten', 'sitting')", "from levenshtein.levenshtein import distance_v2")
print(t.timeit(number=1))

t = Timer("distance_v3('kitten', 'sitting')", "from levenshtein.levenshtein import distance_v3")
print(t.timeit(number=1))

t = Timer("distance_v4('kitten', 'sitting')", "from levenshtein.levenshtein import distance_v4")
print(t.timeit(number=1))

t = Timer("similarity('kitten', 'sitting')", "from levenshtein.clevenshtein import similarity")
print(t.timeit(number=1))
