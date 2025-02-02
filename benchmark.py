from timeit import Timer

t = Timer("distance_v1('kitten', 'sitting')", "from levenshtein.base import distance_v1")
print("V1 =", t.timeit(number=1))

t = Timer("distance_v2('kitten', 'sitting')", "from levenshtein.base import distance_v2")
print("V2 =", t.timeit(number=1))

t = Timer("distance_v3('kitten', 'sitting')", "from levenshtein.base import distance_v3")
print("V3 =", t.timeit(number=1))

t = Timer("distance_v4('kitten', 'sitting')", "from levenshtein.base import distance_v4")
print("V4 =", t.timeit(number=1))

t = Timer("similarity('kitten', 'sitting')", "from levenshtein.c.clevenshtein import similarity")
print("C =", t.timeit(number=1))

t = Timer("similarity('kitten', 'sitting')", "from levenshtein_rs import similarity")
print("RUST =", t.timeit(number=1))