import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from adjustText import adjust_text
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

df = pd.read_csv('robots.csv')

# Plot.
fig, ax = plt.subplots( figsize=(10, 6))
plt.style.use('classic')
marker_sz = 25
font_sz = 21

for i, row in df.iterrows():
    ax.plot(row['Weight'], row['N_actuators'], alpha=0.5, marker='o', markersize=marker_sz, label=row['Name'])

# add numbers to the points
texts = []
for i, row in df.iterrows():
    texts.append(ax.text(row['Weight'], row['N_actuators'], str(i), fontsize=10))
    
# add a legend on the bottom that maps 1 to the first robot, 2 to the second, etc.
legend = ax.legend(ncol=6, loc='lower center', fontsize=12, bbox_to_anchor=(0.5, -0.5))
for i in range(len(df)):
    legend.get_texts()[i].set_text(str(i) + ': ' + df['Name'][i])

sorted_df = df.sort_values(by=['Weight'])
w = np.linspace(1,200,100)
poly = np.polyfit(sorted_df['Weight'], y=sorted_df['N_actuators'], deg=1)
ax.plot(w, np.polyval(poly, w), '--', c='#7F0084', linewidth=1)

plt.xscale('log')
plt.xlabel('Mass [kg]', fontsize=font_sz)
plt.ylabel('No. of actuators', fontsize=font_sz)
plt.xticks(fontsize=font_sz - 5)
plt.yticks(fontsize=font_sz - 5)
plt.tight_layout()
plt.grid(alpha=0.5)
plt.savefig('mass_vs_actuators.png', bbox_inches='tight', dpi=300)
plt.show()
