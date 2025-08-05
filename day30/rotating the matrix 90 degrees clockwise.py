matrix=[[1,2,3],[4,5,6],[7,8,9]]
j=0
while j<len(matrix):
    mat=[]
    for i in matrix:
        mat.append(i[j])
    mat.reverse()
    print(mat)
    j+=1