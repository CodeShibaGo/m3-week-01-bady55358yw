def reverse_string(s):
    # [1:8:2] 代表從索引 1 到 索引 7，而第二字的會忽略 ( 即取 1, 3, 5, 7 )
    # [::-1] 代表從第一個到最後一個，-1代表反轉從後面開始取
    return s[::-1]
result = reverse_string("")
print(result)