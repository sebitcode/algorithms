from clevenshtein import similarity

print(similarity("kitten", "sitting"))  # 61.53846153846154
print(similarity("amor", "amar"))
print(similarity("gato", "atog"))
print(similarity("", ""))     # 100.0
print(similarity("a", ""))    # 0.0
