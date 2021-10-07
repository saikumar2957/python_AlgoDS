R=int(input('enter no.of rows:'))
C=int(input('enter no.of columns:'))
matrix=[]
print('entries for matrix:')
for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=' ')
    print()
