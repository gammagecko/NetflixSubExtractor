# Binary searches for the timestamp
def Binary_Search(arr, time_stamp):
    time_stamp = int(time_stamp)
    if time_stamp < 0 or time_stamp > arr[len(arr) - 1][1]:
        return "Invalid Timestamp"
    low = 0
    high = len(arr) - 1
    low_val = 0
    high_val = arr[high][1]
    while low <= high:

        mid = low + (high - low) // 2
        mid_val = arr[mid][1]

        # Check if time_stamp is present at mid
        if arr[mid][1] <= time_stamp and arr[mid][0] >= time_stamp:
            return arr[mid][2]

        # If x is greater, ignore left half
        elif arr[mid][0] > time_stamp:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid][1] < time_stamp:
            high = mid - 1
    return "Error"
