def distance_v1(word1, word2):
    m, n = len(word1) + 1, len(word2) + 1

    matrix = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        matrix[i][0] = i
    for j in range(n):
        matrix[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            matrix[i][j] = min(  # Minimum of three operations Distance
                matrix[i - 1][j] + 1,  # Insertion
                matrix[i][j - 1] + 1,  # Deletion
                matrix[i - 1][j - 1] + cost,  # Substitution
            )

    similarity = 1 - matrix[-1][-1] / max(m - 1, n - 1)

    return similarity


def distance_v2(word1, word2):
    """Optimized Levenshtein distance with similarity percentage."""
    size1, size2 = len(word1), len(word2)
    max_length = max(size1, size2)

    # Handle empty cases
    if size1 == 0:
        return 100.0 if size2 == 0 else 0.0
    if size2 == 0:
        return 0.0

    # Use two rows to reduce space complexity
    prev_row = list(range(size2 + 1))
    curr_row = [0] * (size2 + 1)

    for i in range(1, size1 + 1):
        curr_row[0] = i
        for j in range(1, size2 + 1):
            substitution_cost = 0 if word1[i - 1] == word2[j - 1] else 1
            curr_row[j] = min(
                prev_row[j] + 1,  # Deletion
                curr_row[j - 1] + 1,  # Insertion
                prev_row[j - 1] + substitution_cost,  # Substitution
            )
        prev_row, curr_row = curr_row, [0] * (size2 + 1)

    similarity = 1 - (prev_row[-1] / max_length)
    return similarity * 100  # Return as percentage


def distance_v3(word1, word2):
    """Optimized Levenshtein distance with similarity percentage."""
    if word1 == word2:
        return 100.0  # Early exit for identical words

    # Swap to use the shorter word for the inner loop
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    len1, len2 = len(word1), len(word2)
    max_len = max(len1, len2)

    if len1 == 0:
        return 100.0 if len2 == 0 else 0.0  # Handle empty cases
    if len2 == 0:
        return 0.0

    # Use a single row for DP, initialized with 0..len2
    row = list(range(len2 + 1))

    for i in range(1, len1 + 1):
        prev, char1 = row[0], word1[i - 1]
        row[0] = i  # Initialize first column for current row

        for j in range(1, len2 + 1):
            sub_cost = 1 - (char1 == word2[j - 1])  # Arithmetic substitution cost
            current = row[j]

            # Compute costs for deletion, insertion, substitution
            row[j] = min(
                current + 1,        # Deletion (from row[j] before update)
                row[j - 1] + 1,     # Insertion (current row's previous)
                prev + sub_cost     # Substitution (diagonal)
            )
            prev = current  # Track diagonal for next iteration

    similarity = (1.0 - row[-1] / max_len) * 100
    return similarity


def distance_v4(word1, word2):
    """Optimized Levenshtein distance with similarity percentage."""
    if word1 == word2:
        return 100.0  # Early exit for identical words

    if not (word1 and word2):
        return 0.0  # Handle empty cases

    # Swap to use the shorter word for the inner loop
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    len1, len2 = len(word1), len(word2)

    # Use a single row for DP, initialized with 0..len2
    row = list(range(len2 + 1))

    for i in range(1, len1 + 1):
        prev, char1 = row[0], word1[i - 1]
        row[0] = i  # Initialize first column for current row

        for j in range(1, len2 + 1):
            sub_cost = 1 - (char1 == word2[j - 1])  # Arithmetic substitution cost
            current = row[j]

            # Compute costs for deletion, insertion, substitution
            row[j] = min(
                current + 1,        # Deletion (from row[j] before update)
                row[j - 1] + 1,     # Insertion (current row's previous)
                prev + sub_cost     # Substitution (diagonal)
            )
            prev = current  # Track diagonal for next iteration

    similarity = (1.0 - row[-1] / max(len1, len2)) * 100
    return similarity
