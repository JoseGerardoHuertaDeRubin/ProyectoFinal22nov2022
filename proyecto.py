from matplotlib import pyplot as plt
import random

def Grafica(VR_data, VGS, VR):
  plt.figure(1)
  plt.plot(VGS,VR_data)
  plt.plot(VGS,VR)
  plt.grid()
  plt.legend(['data','calculated'])
  plt.title('$V_R$ vs $V_{GS}$')
  plt.ylabel('resistor voltage (V)')
  plt.xlabel('gate-to-source voltage (V)')
  plt.show()

def R(m,n,R):
  if m/n > 0.9 and m/n < 1.1:
    nsq = round(n/2)
    msq = (m-2)*nsq +2
    csq = n - nsq
    tsq = msq + csq + 2*(2*csq/3)
    Rt = tsq * R
  else:
    Rt = 0
  return Rt

def ID(beta,W,L,VGS,VT,VDS):
  Id = []
  for x in VGS:
    I = (beta/2)*(W/L)*((x-VT)**2)*(1 + 0.01*VDS)
    Id.append(I)
  return Id

def ECM(VR_data,VR):
  E = 0
  N = len(VR_data)
  for i in range(N):
    E += (VR_data[i]-VR[i])**2
  E = E/N
  return E


#Resistor voltage measured/simulated data
VR_data = [1.00E-07, 2.50E-02, 1.00E-01, 2.25E-01, 4.00E-01, 6.25E-01, \
            9.00E-01, 1.23E+00, 1.57E+00, 1.84E+00, 2.07E+00]


#gate-to-source voltage sweep  
VGS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]


#fixed parameters
VDS = 5         #drain-to-source voltage  
VT = 0.69       #treshold voltage (for silicon)
beta = 4.5e-6   #transistor's beta 
rsq = 25        #sheet resistance, ohms per square


#transistor variables
W = 24e-6        #gate width
L = 9e-6        #gate length
print('W: '+str(round(1e6*W,1))+'μm\t'+'L: '+str(round(1e6*L,1))+'μm')


#resistor
m = 40          #resistor squares per line
n = 40          #resistor lines
Ri = R(m,n,rsq)          # R(rsq, m, n)
print("R:", Ri, 'Ω')

#specifications
c_len = 14
n_pop = 32
gen = 300





#transistor's drain current I_D (for each V_GS value)
I_D = ID(beta,W,L,VGS,VT,VDS)

#resistor voltage V_R = I_D * R
VR = []
for i in I_D:
  VR.append(Ri*i)

# mean square error
MSE = ECM(VR_data,VR)
print("mean sq error: ", round(MSE, 7))
Grafica(VR_data, VGS, VR)