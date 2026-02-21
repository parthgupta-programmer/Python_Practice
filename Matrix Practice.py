# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix)
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j],end="")
#     print()
matrix=[]
n=int(input("Enter the no.of rows:"))
c=int(input("Enter the no.of columns:"))
print("Now,enter the elements of the matrix:")
for i in range(n):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
print(matrix)