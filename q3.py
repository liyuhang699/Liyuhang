# 按照题意，我认为示例输入的[1,3,5,9]的最大权值子序列应该是1.33，子序列是[1,3,9]
# val(S) : Mean(S)-Median(S)

# 复杂度为n^2
def maxVal(n, a):
    a.sort()
    max_val = -100000
    for idx_median in range(0,n,1):
        # 中位数为a[idx_median]的情况下，寻找最大的mean值即可
        # print("中位数：",a[idx_median])
        # 中位数序号k除以2下取整
        # 因此中位数的左边可以比右边多一个数
        num_left = idx_median
        num_right = n - idx_median - 1
        sum = a[idx_median]
        k = 1
        max_mean = a[idx_median]
        for i in range(1,num_left+1,1):
            # 左边增加一个数，由于num_left = idx_median所以一定在范围内
            sum += a[idx_median-i]
            k += 1
            #print("增加",a[idx_median-i],",mean=",sum/k)
            max_mean = max(max_mean,sum/k)
            # 右边增加一个数
            if(i <= num_right):#不越界
                sum += a[n-i] #先加大的数
                k += 1
                #print("增加",a[n-i],",mean=",sum/k)
                max_mean = max(max_mean,sum/k)
            else: break
        max_val = max(max_val,max_mean-a[idx_median])
        #print("max_val=",max_val)
    return max_val


n = 4
a = [1, 3, 5, 9]
print(maxVal(n, a))
