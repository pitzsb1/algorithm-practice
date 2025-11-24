def solution(arr):
    info = {"last": None} 
    result = []

    for num in arr:
        if info["last"] != num:
            result.append(num)
        info["last"] = num

    return result
