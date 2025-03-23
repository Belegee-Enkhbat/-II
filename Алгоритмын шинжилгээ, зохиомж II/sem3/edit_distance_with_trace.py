def edit_distance_with_trace(s1, s2):
    m, n = len(s1), len(s2)

    d = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + cost)

    distance = d[m][n]

    i, j = m, n
    aligned_s1 = []
    aligned_s2 = []
    operations = []

    while i > 0 or j > 0:
        current_cost = d[i][j]

        if (
            i > 0
            and j > 0
            and d[i - 1][j - 1] <= d[i][j - 1]
            and d[i - 1][j - 1] <= d[i - 1][j]
        ):
            diag_cost = d[i - 1][j - 1]
            if current_cost == diag_cost:
                aligned_s1.append(s1[i - 1])
                aligned_s2.append(s2[j - 1])
                operations.append("|")
            else:
                aligned_s1.append(s1[i - 1])
                aligned_s2.append(s2[j - 1])
                operations.append("*")
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or d[i][j - 1] < d[i - 1][j]):
            aligned_s1.append("-")
            aligned_s2.append(s2[j - 1])
            operations.append(" ")
            j -= 1
        else:
            aligned_s1.append(s1[i - 1])
            aligned_s2.append("-")
            operations.append(" ")
            i -= 1

    aligned_s1.reverse()
    aligned_s2.reverse()
    operations.reverse()

    print("DP matrix (edit distances) =")
    for row in d:
        print(row)

    print("\nAlignment:")
    print("s1:", " ".join(aligned_s1))
    print("    ", " ".join(operations))
    print("s2:", " ".join(aligned_s2))

    return distance


if __name__ == "__main__":
    s1 = "mongolia"
    s2 = "ogota"
    dist = edit_distance_with_trace(s1, s2)
    print(f"\nEdit distance between '{s1}' and '{s2}': {dist}\n")

    s3 = "flaw"
    s4 = "lawn"
    dist = edit_distance_with_trace(s3, s4)
    print(f"\nEdit distance between '{s3}' and '{s4}': {dist}\n")

    s5 = "abcdef"
    s6 = "azced"
    dist = edit_distance_with_trace(s5, s6)
    print(f"\nEdit distance between '{s5}' and '{s6}': {dist}")
