def max_sub_sum(nums: list) -> int:
    condensed = []
    curr = nums[0]
    temp_max = curr
    for i in range(1, len(nums)):
        temp_max = max(temp_max, nums[i])
        if curr * nums[i] >= 0:
            curr += nums[i]
        else:
            condensed.append(curr)
            curr = nums[i]
    condensed.append(curr)
    print(condensed)

    if len(condensed) == 1:
        return max(temp_max, max(condensed))
    
    idx = 0
    if condensed[0] < 0:
        idx += 1
    
    temp_sum = condensed[idx]
    while idx < len(condensed):
        print(f"temp_max : {temp_max}, temp_sum : {temp_sum}")
        if idx + 2 < len(condensed):
            if temp_sum + condensed[idx+1] + condensed[idx+2] > 0:
                temp_sum += condensed[idx+1] + condensed[idx+2]
            else:
                temp_max = max(temp_max, temp_sum)
                temp_sum = condensed[idx+2]
        idx += 2

    return max(temp_max, temp_sum)


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_sub_sum(nums))