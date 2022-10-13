import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

prefactor = (1/137)**2/(4*14**2)

def term1(costheta):
    return prefactor*2*((1 + costheta)**2 + 4)/(1 - costheta)**2

def term2(costheta):
    return prefactor*(1 + costheta**2)

def term3(costheta):
    return -prefactor*2*(1 + costheta)**2/(1 - costheta)

def dsigmadOmega(costheta):
    return term1(costheta) + term2(costheta) + term3(costheta)

costheta = np.linspace(-1, 0.9999, 10000)

alpha=0.5

sns.set()
plt.plot(costheta, dsigmadOmega(costheta), color='black', label=r'$\langle \vert \mathcal{M} \vert ^2 \rangle$')
plt.plot(costheta, term1(costheta), color='blue', alpha=alpha, linestyle='dashed', label=r'$\vert \mathcal{M}_1 \vert ^2$')
plt.plot(costheta, term2(costheta), color='red', alpha=alpha, linestyle='dashed', label=r'$\vert \mathcal{M}_2 \vert ^2$')
plt.plot(costheta, term3(costheta), color='orange', alpha=alpha, linestyle='dashed', label=r'$\mathcal{M}^{\dagger}_1\mathcal{M}_2 + \mathcal{M}^{\dagger}_2\mathcal{M}_1$')
plt.xlabel(r'$\cos\theta$')
plt.ylabel(r'$d \sigma/d \Omega \hspace{1} [\mathrm{GeV}^{-2}]$')
plt.yscale('symlog', linthresh=0.000001)
plt.legend()
plt.title(r'$e^- e^+ \rightarrow e^- e^+$ cross section')
plt.tight_layout()
plt.savefig("electron-positron-scattering.pdf", format='pdf')