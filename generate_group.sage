CF.<z> = CyclotomicField(8)

ii = z**2
s2 = z**7+z

M1 = 1/s2*Matrix(CF,[[1,1],[1,-1]])
M2 = diagonal_matrix([1,ii])

G = MatrixGroup([M1,M2])
