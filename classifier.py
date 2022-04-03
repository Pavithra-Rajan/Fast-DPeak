from FastDPeak import FastDPeak

df = pd.read_csv('IRIS.csv')
X=df.values[:,:4]
Y= df.values[:,[4]]

def distance(p,q):
    s=0
    for i in range(len(p)):
        s+=((p[i]-q[i])**2)
    return s**(1/2)

