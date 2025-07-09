## 재귀를 통해서 풀면 좋을 것 같다!!


def dfs(n, nums):
    if n == k:
        nums_str = nums.replace(' ', '')
        if eval(nums_str) == 0:
            results.append(nums)
        return
    
    next_n = str(n + 1)
    dfs(n + 1, nums + ' ' + next_n)
    dfs(n + 1, nums + '+' + next_n)
    dfs(n + 1, nums + '-' + next_n)

t = int(input())
for _ in range(t):
    k = int(input())
    results = []
    dfs(1, "1")
    for r in sorted(results):
        print(r)
    print()

