def minSubsequences(source, target):
    seq_count = 0
    idx_target = 0 # target的指针
    L_target = len(target)
    L_source = len(source)

    while idx_target < L_target:
        seq_count += 1
        idx_source = 0  # source的指针
        found_flag = 0  # 判断是否能做到

        while idx_source < L_source and idx_target < L_target:
            if source[idx_source] == target[idx_target]:
                idx_target += 1
                found_flag = 1
            idx_source += 1

        if found_flag == 0:
            return -1

    return seq_count

source = "abc"
target = "abcbc"
print(minSubsequences(source, target))

source = "abc"
target = "acdbc"
print(minSubsequences(source, target)) 

source = "xyz"
target = "xzyxz"
print(minSubsequences(source, target)) 

source = "123456789"
target = "19273645"
print(minSubsequences(source, target)) 