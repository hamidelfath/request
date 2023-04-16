def obtain_coef(fl1,fl2,fr1,fr2,V):
    
    #left 1 and right 1
    cfl1 = [fl1.monomial_coefficient(v) for v in V]
    cfr1 = [fr1.monomial_coefficient(v) for v in V]
    

    #left 2 and right 2
    cfl2 = [fl2.monomial_coefficient(v) for v in V]
    cfr2 = [fr2.monomial_coefficient(v) for v in V]
    
    Eq = [c1-c2 for c1,c2 in zip(cfl1,cfr1)]
    Eq += [c1-c2 for c1,c2 in zip(cfl2,cfr2)]

    return Eq

def mat_coef(Eq,V1):
    Co = []
    for eq in Eq:
        co = [eq.monomial_coefficient(v) for v in V1]
        Co.append(co)
    M = Matrix(Co)
    return M

