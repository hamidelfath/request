load('generate_group.sage')
load('poly_function.py')

n = int(input('enter the degree:'))

for i in range(n):
    [f1,f2,V] = ff(i)
    Mat1 = mat_poly(f1,f2,V,M1)
    Mat2 = mat_poly(f1,f2,V,M2)
    
    MM = block_matrix([[Mat1],[Mat2]],subdivide=False)
    if len(V)>MM.rank():
        print(i,len(V),MM.rank())
