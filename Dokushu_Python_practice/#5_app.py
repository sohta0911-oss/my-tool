# main_app.py
import vector_tools

a=[1,2,2]
b=[5,4,2]

# 「モジュール名.関数名」で呼び出す
similarity, label = vector_tools.calculate_cosine_similarity(a, b)

print(f"Result: {similarity} ({label})")