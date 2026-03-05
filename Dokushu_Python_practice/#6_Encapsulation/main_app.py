# main_app.py
import vector_tools

v1 = vector_tools.Vector([1, 2, 2])
v2 = vector_tools.Vector([10, 4, 2])

print(f"L2 norm of vector v1: {v1.l2_norm()}")
print(f"L2 norm of vector v2: {v2.l2_norm()}")
print(f"similality: {v1.similality(v2, threshold=0.8)}")


a = [1,2,2]
b = [5,4,2]

similarity, label = vector_tools.calculate_cosine_similarity(a, b)

print(f"Result: {similarity} ({label})")