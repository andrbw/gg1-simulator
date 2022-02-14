#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_table("result.dat", sep=' ', index_col=None, header=0)

plt.figure(figsize=[12, 9], dpi=120)

plt.errorbar(df['Lambda'], df['ServiceTimeMean'], df['ServiceTimeConfInterval'], marker='x', linestyle='None', color='k', label='simulation')

lam_mu = np.arange(0.05, 0.96, 0.01)
service_time = 1. / (1. - lam_mu)
plt.plot(lam_mu, service_time, marker='None', linestyle='-', color='k', label='analytics')

plt.xlabel(r'$\lambda / \mu$', fontsize=20)
plt.ylabel('Average service time', fontsize=20)
plt.tick_params(labelsize=15)
plt.grid()
plt.legend(loc='best', fontsize=20)
plt.tight_layout()
plt.savefig("service_time.png")
