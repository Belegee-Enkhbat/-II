def lcs_length_and_sequence(X, Y):
    print(X, Y)
    m, n = len(X), len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]

    lcs_seq = []
    i, j = m, n

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_seq.append(X[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    lcs_seq.reverse()
    return lcs_length, "".join(lcs_seq)


X1, Y1 = "ABCD", "AEBD"
length1, seq1 = lcs_length_and_sequence(X1, Y1)
print(length1, seq1)

X2, Y2 = "ABC", "ABC"
length2, seq2 = lcs_length_and_sequence(X2, Y2)
print(length2, seq2)

X3, Y3 = "AGCCCTAAGGGCTACCTAGCTT", "GACAGCCTACAAGCGTTAGCTTG"
length3, seq3 = lcs_length_and_sequence(X3, Y3)
print(length3, seq3)
