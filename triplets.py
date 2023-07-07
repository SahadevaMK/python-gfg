arr = [1, 5, 3, 2, 6]
count = 0
N = len(arr)
index = [0] * (max(arr) + 1)

for i in range(N):
    index[arr[i]] = 1

for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] + arr[j] < len(index) and index[arr[i] + arr[j]] == 1:
            count += 1

print(count)
