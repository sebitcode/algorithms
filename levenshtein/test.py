from c.clevenshtein import similarity as c
from levenshtein_rs import similarity as rs

print(c("kitten", "sitting"))  # 61.53846153846154
print(c("amor", "amar"))
print(c("gato", "atog"))
print(c("", ""))     # 100.0
print(c("a", ""))    # 0.0


print(rs("kitten", "sitting"))  # 57.14285714285714
print(rs("", "test"))           # 0.0
print(rs("identical", "identical"))  # 100.0