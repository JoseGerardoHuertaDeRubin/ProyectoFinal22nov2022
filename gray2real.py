def gray2real(indiv):
    g0 = indiv[0:7]
    g1 = indiv[7:14]
    g2 = indiv[14:20]
    g3 = indiv[20:26]
    
    b0 = [g0[0]]
    b1 = [g1[0]]
    b2 = [g2[0]]
    b3 = [g3[0]]
    
    for i in range(6):
      b0.append(int(b0[i])^int(g0[i+1]))
      b1.append(int(b1[i])^int(g1[i+1]))
    for i in range(5):
      b2.append(int(b2[i])^int(g2[i+1]))
      b3.append(int(b3[i])^int(g3[i+1]))
    
    r0 = 0
    r1 = 0
    r2 = 0
    r3 = 0
    
    for i in range(len(b0)):
        r0 += b0[i]*2**(6-i)
        r1 += b1[i]*2**(6-i)
    
    for i in range(len(b2)):
        r2 += b2[i]*2**(5-i)
        r3 += b3[i]*2**(5-i)
    
    r0 = ((0.3 * r0) + 0.6)*1e-6
    r1 = ((0.3 * r2) + 0.6)*1e-6
    r2 = r2 + 1
    r3 = r3 + 1
    
    R = [r0, r1, r2, r3]
    
    return R