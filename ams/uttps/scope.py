import numpy as np
from math import sqrt

f = open('d', 'rb')
data = f.read()
f.close()

print("len(data) = ", str(len(data)))

data_us = []
data_us_len = int(len(data)/2.)
k = 0
for i in range(data_us_len): 
    j = i*2 # index of unsigned short array
    d_us = (0x00FF & data[j] | ( (0x00FF & data[j+1]) << 8) )
    if (d_us & 0x8000 != 0) and (k == 0):
        k = i

    data_us.append(d_us)
    i+=2 # step 2, over bytes array

print('len(data_us) = {}'.format(data_us_len))
print('data[{:2d}] = {:#x}'.format(k, data_us[k]))

m = 18 # number of sectors 
turns = data_us[k:] 
nturns = int(len(turns)/m -1) # why -1? 
print('nturns = {}'.format(nturns))
print('len(turns) = {}'.format(len(turns)))
print('2273 * 18 = {}'.format(2273 * 18))

nsectors = m * nturns # total number of sectors
sum1 = np.zeros(m) # sum of sector_values over all turns
sum2 = np.zeros(m) # sum of sector_v_squares over all turns
print(nturns)

for j in range(nturns):
    turn = turns[ j*m : (j+1)*m ] # 18 sectors of each turn
    for i in range(m):
        sector_value = turn[i]
        v = ( (0x7FFF & sector_value) +0.5 ) /5.0
        sum1[i] += v
        sum2[i] += v * v

sectorM = np.sum(sum1) / nsectors
Srpm = 60. * 1000000. / (m * sectorM)
print('Nturns={:d} RPM={:7.1f} sec ava={:6.2f} nsectors={:8d}\n'.format(
    nturns,
    Srpm,
    sectorM,
    nsectors))

for i in range(m):
    s_i = sum1[i]/nturns
    m_i = sectorM - s_i
    v_i = 100. * m_i / sectorM
    x = (sum2[i] - pow(sum1[i],2)/nturns ) / nturns
    sigma_i = sqrt( x )
    print( 'sec {a0:2d}  {a1:7.2f} usec  {a2:7.2f}  {a3:5.1f}   {a4:5.2f}'.format(
        a0 = i,
        a1 = s_i,
        a2 = m_i,
        a3 = v_i,
        a4 = sigma_i
    ))

