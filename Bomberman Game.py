input_grid =['.......','...O.O.','....O..','..O....','OO...OO','OO.O...']
r=6
c=7
n=5
output_grid=[]

matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(input_grid[i][j])
    matrix.append(a)
    # print(matrix[i])


for i in range(1,n+1):
    print("After ",i,"second :")
    for j in range(r):# r=6
        for k in range(c):# c=7
            if(matrix[j][k]=="O"):
                matrix[j][k]="O1"
            elif(matrix[j][k]=="." and i%2==0):
                matrix[j][k]="O"
            elif(matrix[j][k]=="O2"):
                matrix[j][k]="."
                l1=[[j+1,k],[j-1,k],[j,k+1],[j,k-1]]
                for u in range(4):
                    x,y=l1[u]
                    if(0 <= x < r and 0 <= y < c and matrix[x][y]!="O2"):
                        matrix[x][y]="."
            elif(matrix[j][k]=="O1"):
                matrix[j][k]="O2"
            print(matrix[j][k],end="")

        print()



for i in range(r):
    st=""
    for j in range(c):
        if(matrix[i][j]=="O" or matrix[i][j]=="O1" or matrix[i][j]=="O2"):
            matrix[i][j]="O"
            st+=matrix[i][j]
        else:
            st+=matrix[i][j]
    output_grid.append(st)

print(output_grid)