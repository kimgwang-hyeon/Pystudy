N = int(input())
used = set()

for _ in range(N):
    line = input()
    words = line.split()
    found = False

    for i, word in enumerate(words):
        key = word[0].lower()
        if key not in used:
            used.add(key)
            words[i] = f'[{word[0]}]{word[1:]}'
            found = True
            print(' '.join(words))
            break

    if not found:
        for i, ch in enumerate(line):
            if ch == ' ':
                continue
            key = ch.lower()
            if key not in used:
                used.add(key)
                line = line[:i] + f'[{ch}]' + line[i+1:]
                print(line)
                break
        else:
            print(line)
