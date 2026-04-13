x = 0.2 * 3
y = 0.6

print(x == y)      # おそらく False が出る
print(x)           # 実際の中身を見てみよう
print(abs(x - y) < 0.0001) # これなら True になる


def heavy_process():
    print("重たい計算を実行中...")
    return True

# 左側が False なので、heavy_process は実行されない（文字が表示されない）
print(False and heavy_process())

print("---")

# 左側が True なので、heavy_process が実行される
print(True and heavy_process())