def merge(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    lenA = len(arr1)

    newArr1 = arr[:lenA]
    newArr2 = arr[lenA:]

    print(newArr1)
    print(newArr2)

arr1 = [2,4,7,10]
arr2 = [2,3]
merge(arr1, arr2)

