import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = 0.98
alpha = 1/137

F1 = a*(a**4 + 26*a**3 -75)/(3*(a**2 - 1)) + 8*np.log((a - 1)/(-a - 1))

F2 = a*(a**2 + 3)/3

def cross_section(sqrt_s, F):
    return np.pi*alpha**2/sqrt_s**2*F

sqrt_s = np.linspace(5, 30, 100)

sns.set()
plt.plot(sqrt_s, cross_section(sqrt_s, F1), label=r'$e^-e^+ \rightarrow e^-e^+$')
plt.plot(sqrt_s, cross_section(sqrt_s, F2), label=r'$e^-e^+ \rightarrow \mu^- \mu^+$')
plt.xlabel(r'$\sqrt{s} \hspace{1} [\mathrm{GeV}]$')
plt.ylabel(r'$\sigma \hspace{1} [\mathrm{GeV}^{-2}]$')
plt.yscale('log')
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("total-cross-sections.pdf", format='pdf')