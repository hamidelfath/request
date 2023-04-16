def ff(n):
    st_var = [str('a')+str(i) for i in range(n+1)]
    st_var += [str('b')+str(i) for i in range(n+1)]
    vR = ','.join(st_var)
    R = PolynomialRing(CF,vR)
    R.inject_variables()
    a = R.gens()[0:n+1]
    b = R.gens()[n+1:len(R.gens())]

    Rxy = PolynomialRing(R,'x,y')
    Rxy.inject_variables()
    
    f1 = Rxy(sum([x**(n-i)*y**(i)*a[i] for i in range(n+1)]))
    f2 = Rxy(sum([b[i]*x**(n-i)*y**(i) for i in range(n+1)]))
    
    V = a+b
    return [f1,f2,V]

def leftside(f1,f2,M):
    #M is the matrix related to the invariant
    #f is the function
    dsu = {x:M[0,0]*x+M[0,1]*y,y:M[1,0]*x+M[1,1]*y}
    lf1 = f1.subs(dsu)
    lf2 = f2.subs(dsu)

    return [lf1,lf2]

def rightside(f1,f2,M):
    rf1 = M[0,0]*f1+M[0,1]*f2
    rf2 = M[1,0]*f1+M[1,1]*f2

    return [rf1,rf2]

def mat_poly(f1,f2,V,M):
    lf = matrix(leftside(f1,f2,M))
    rf = matrix(rightside(f1,f2,M.inverse()))

    mc = lf-rf
    Eq = mc[0,0].coefficients()
    Eq+=mc[0,1].coefficients()
    
    Co = []
    for eq in Eq:
        co = [eq.monomial_coefficient(m) for m in V]
        Co.append(co)
    return matrix(Co)

    
