A = {'a', 'n', 'e', 't', 'x', 'y', 'n', 'w'}
B = {'p', 'y', 't', 'h', 'o', 'n'}

# 합집합 구하기
print(A.union(B))
print(A | B)

# 교집합 구하기
print(A.intersection(B))
print(A & B)

# 차집합 구하기
print(A.difference(B))
print(A - B)

# 대칭차집합 구하기
print(A.symmetric_difference(B))
print(A ^ B)
