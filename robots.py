import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from adjustText import adjust_text
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


df = pd.read_csv('robots.csv')
print(df.head())
print(df.columns)

# Plot.
fig, ax = plt.subplots()
# fig.set_size_inches(5, 3)
plt.style.use('classic')
marker_sz = 20
font_sz = 10

# def add_image(ax, img_path, x, y, zoom=0.05):
#     """Adds an image at (x, y) coordinates."""
#     img = plt.imread(img_path)
#     ax.add_patch(plt.Circle((x, y), 3.0, color='red', alpha=0.5))
#     imagebox = OffsetImage(img, zoom=zoom)
#     ab = AnnotationBbox(imagebox, (x, y), frameon=False)
#     ax.add_artist(ab)
# Add images as markers
# for i in range(len(df)):
#     print(df['Image'][i])
#     if df['Image'][i] is not np.nan:
#         path = 'images/' + df['Image'][i]
#         add_image(ax, path, df['Weight'][i], df['N_actuators'][i])

# Combinations of marker styles and colors:
for i, row in df.iterrows():
    ax.plot(row['Weight'], row['N_actuators'], alpha=0.8, marker='o', markersize=marker_sz, label=row['Name'])

sorted_df = df.sort_values(by=['Weight'])
w = np.linspace(1,200,100)
poly = np.polyfit(sorted_df['Weight'], y=sorted_df['N_actuators'], deg=1)
ax.plot(w, np.polyval(poly, w), '--', c='#7F0084', linewidth=1)
# ax.set_xlim([1, 250])
# ax.set_ylim([4, 65])
plt.xscale('log')
# # plt.legend(loc="lower center", bbox_to_anchor=(0.29, 0), fontsize=7)
plt.xlabel('Mass [kg]', fontsize=font_sz)
plt.ylabel('No. of actuators', fontsize=font_sz)
plt.tight_layout()
plt.legend()
plt.savefig('mass_vs_actuators.pdf', bbox_inches='tight')
plt.show()
