def main():
    s = input()
    n = len(s)
    v = [[]] * n
    used = [False] * 256
    now = 0

    for i in range(n):
        if s[i] == "(":
            now += 1
        elif s[i] == ")":
            for c in v[now]:
                used[ord(c) - ord('a')] = False
            v[now].clear()
            now -= 1
        else:
            if used[ord(s[i]) - ord('a')]:
                print("No")
                return
            v[now].append(s[i])
            used[ord(s[i]) - ord('a')] = True

    print("Yes")


if __name__ == '__main__':
    main()
