def caliculate_innner_product(a, b):
    if len(a) != len(b):
        raise ValueError("ベクトルの次元が一致しません")
    
    inner_product = sum(x * y for x, y in zip(a, b))
    return inner_product

# ベクトルの定義
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
# 内積の計算
result = caliculate_innner_product(vector_a, vector_b)
print("内積:", result)