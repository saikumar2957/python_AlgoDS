m = 4 
n = 4 
r = 2
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(min(m,n)//2):
        stack = []
        for i1 in range(i+1,m-i):
            stack.append(mat[i1][i])
        for i1 in range(i+1,n-i):
            stack.append(mat[m-i-1][i1])
        for i1 in range(m-i-2,i-1,-1):
            stack.append(mat[i1][n-i-1])
        for i1 in range(n-i-2,i-1,-1):
            stack.append(mat[i][i1])
        if len(stack) == 0:
            break
        r1 = r%(len(stack))
        stack = stack[(len(stack)-r1):]+stack[:(len(stack)-r1)]
        t = 0
        for i1 in range(i+1,m-i):
            mat[i1][i] = stack[t]
            t+=1
        for i1 in range(i+1,n-i):
            mat[m-i-1][i1] = stack[t]
            t+=1
        for i1 in range(m-i-2,i-1,-1):
            mat[i1][n-i-1] = stack[t]
            t+=1
        for i1 in range(n-i-2,i-1,-1):
            mat[i][i1] = stack[t]
            t+=1
for a in mat:
    print(*a)