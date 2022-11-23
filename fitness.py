def fitness(RR):
    VR = []
    w = RR[0]
    l = RR[1]
    me = RR[2]
    ne = RR[3]
    Re = R(me,ne,rsq)
    Id = ID(beta,w,l,VGS,VT,VDS)
    for i in Id:
      VR.append(Re*i)
    MSE = ECM(VR_data,VR)
    return MSE