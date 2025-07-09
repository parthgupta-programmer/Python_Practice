input_grid =['.......', '...O...', '....O..','.......', 'OO.....', 'OO.....']
r=6
c=7
n=3
output_grid=""
# .......         
# ...O...                
# ....O..
# .......
# OO.....
# OO.....

matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(input_grid[i][j])
    matrix.append(a)
    print(matrix[i])

for i in range(n):
    for j in range(r):
        for k in range(c):
            if(matrix[j][k]=="O"):
                matrix[j][k]="O"+str(i+1)
print(matrix)