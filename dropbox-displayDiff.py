def solution(oldVersion, newVersion):
    def diffHelper(s1, s2):
        def lcs(a, b):
            m, n = len(a), len(b)
            dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if a[i-1] == b[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            lcs_str = ""
            while m > 0 and n > 0:
                if a[m-1] == b[n-1]:
                    lcs_str = a[m-1] + lcs_str
                    m, n = m-1, n-1
                elif dp[m-1][n] > dp[m][n-1]:
                    m -= 1
                else:
                    n -= 1
            return lcs_str

        lcs_str = lcs(s1, s2)
        result, i, j = "", 0, 0
        old_chars, new_chars = "", ""
        for char in lcs_str:
            while i < len(s1) and s1[i] != char:
                old_chars += s1[i]
                i += 1
            if old_chars:
                result += "(" + old_chars + ")"
                old_chars = ""
            while j < len(s2) and s2[j] != char:
                new_chars += s2[j]
                j += 1
            if new_chars:
                result += "[" + new_chars + "]"
                new_chars = ""
            result += char
            i += 1
            j += 1
        if i < len(s1):
            result += "(" + s1[i:] + ")"
        if j < len(s2):
            result += "[" + s2[j:] + "]"
        return result

    return diffHelper(oldVersion, newVersion)
