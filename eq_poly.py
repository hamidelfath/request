load('generate_group.sage')
R1 = PolynomialRing(CF,'a,b,c,d')
R1.inject_variables()
R = PolynomialRing(R1,'x,y')
R.inject_variables()

V = [x,y]
V1 = R1.gens()
#var('a,b,c,d,e,f')

G = [M1,M2]
#G = [M2]
f1 = a*x + b*y
f2 = c*x + d*y

#f1 = a*x**2 + b*x*y + c*y**2
#f2 = d*x**2 + e*x*y + f*y**2
LM = []

for g in G:
    h = g
    #h = g.matrix()
    #dictionary of substitution
    dsu = {x:h[0,0]*x+h[0,1]*y,y:h[1,0]*x+h[1,1]*y}
    fl1 = f1.subs(dsu)
    fl2 = f2.subs(dsu)

    fr1 = h[0,0]*f1+h[0,1]*f2
    fr2 = h[1,0]*f1+h[1,1]*f2

    Eq = obtain_coef(fl1,fl2,fr1,fr2,V)
    M = mat_coef(Eq,V1)
    LM.append(M)
