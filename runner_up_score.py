if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
    length = len(arr1)
    arr1.sort()
    i = length - 1
    while i >= 0:
        if arr1[i] < arr1[-1]:
            print(arr1[i])
            break
        i -= 1
