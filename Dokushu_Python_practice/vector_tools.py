#vector_tools.py

def calculate_inner_product(a,b):
    # 内積の定義
    if len(a) !=len(b):
        raise ValueError("ベクトルの次元が一致しません")
    
    inner_product = sum(x*y for x,y in zip(a,b))
    return inner_product


def calculate_l2_norm(a):
    # L2ノルムの定義
    return sum(x**2 for x in a)**0.5


def calculate_cosine_similarity(a,b, threshold=0.8):
    """
    Calculate the cosine similarity between two vectors.
    
    Args:
        a, b (list): Input vectors.
        threshold (float): Similarity threshold (default: 0.8).
        
    Returns:
        tuple: (similarity_score, status_label)
    """

    inner_product = calculate_inner_product(a,b)
    norm_a = calculate_l2_norm(a)
    norm_b = calculate_l2_norm(b)

    if norm_a == 0 or norm_b == 0: #0除算を防ぐ！
        raise ValueError("ベクトルのノルムがゼロです")
    
    cosine_similarity = inner_product / (norm_a * norm_b)

    if cosine_similarity > threshold:
        status = "similar"
    else:
        status = "not similar"
    
    return cosine_similarity, status


# ベクトルの定義
a=[1,2,2]
b=[5,4,2]

print("Inner product:", calculate_inner_product(a,b))
print("L2 norm of a:", calculate_l2_norm(a))
print("L2 norm of b:", calculate_l2_norm(b))
print("Cosine similarity:", calculate_cosine_similarity(a,b,threshold=0.85))