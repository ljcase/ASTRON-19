from scipy.stats import ttest_ind
import numpy as np
import matplotlib.pyplot as plt

def pvaule(x0,x1):

    _,p = ttest_ind(x0,x1,,equal_var=False)

    return p
nsamples = 100



x0 = np.random.normal(loc=0,scale=1.0,size=nsamplees)
x1 = np.random.normal(loc=0,scale=1.0,size=nsamplees)

f, ax = plt.subplots(1,1,figsize=(7,7))
ax.xaxis.set_tick_params(whitch='both',direction='in')
ax.yaxis.set_tick_params(whitch='both',direction='in')
ax.hist(x0,bins=10,alpha=0.5,label='Set A')
ax.hist(x1,bins=10,alpha=0.5,label='Set B')
plt.legend(frameon=False)

p = pvalue(x0,x1)
print(f'The pvalue fo the null hypothosis that x0 and x1 are pulled from the same distrabution is p={p:5.4e}.')

