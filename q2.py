def bracketDetect(str):
    str_seq = str.split('\n')
    for sub_str in str_seq:
        L = len(sub_str)
        mark = [' '] * L
        
        match_right = 0 # 记录是否有多余的右括号
        match_left = 0 # 记录是否有多余的左括号

        for i in range(0,L,1):
            # 正向扫描多余的右括号
            if sub_str[i] == '(':
                match_right += 1
            elif sub_str[i] == ')':
                match_right -= 1
                if match_right < 0:
                    mark[i] = '?'
                    match_right = 0
            # 反向扫描多余的左括号
            if sub_str[L-1-i] == ')':
                match_left += 1
            elif sub_str[L-1-i] == '(':
                match_left -= 1
                if match_left < 0:
                    mark[L-1-i] = 'x'
                    match_left = 0
        print(sub_str)
        for c in mark:
            print(c,end="")
        print()


input = "bge)))))))))\n((IIII))))))\n()()()()(uuu\n))))UUUU((()"
bracketDetect(input)