import matplotlib.pyplot as plt
import pandas as pd

# Load data from TSV files
familiarity = pd.read_csv(r"C:\Users\laugh\OneDrive\Gen-AI-For-Game-Designers\Code\familiarity.tsv", sep='\t')
ease_of_use = pd.read_csv(r"C:\Users\laugh\OneDrive\Gen-AI-For-Game-Designers\Code\ease_of_use.tsv", sep='\t')
versatility = pd.read_csv(r"C:\Users\laugh\OneDrive\Gen-AI-For-Game-Designers\Code\versatility.tsv", sep='\t')
time_saving = pd.read_csv(r"C:\Users\laugh\OneDrive\Gen-AI-For-Game-Designers\Code\time_saving.tsv", sep='\t')

# Set up subplots
fig, ax = plt.subplots(2, 2, figsize=(14, 10))

# Plot Familiarity
ax[0, 0].barh(familiarity['Tool'], familiarity['Familiarity'], color='skyblue')
ax[0, 0].set_title('Familiarity')

# Plot Ease of Use
ax[0, 1].barh(ease_of_use['Tool'], ease_of_use['Ease of Use'], color='lightgreen')
ax[0, 1].set_title('Ease of Use')

# Plot Versatility
ax[1, 0].barh(versatility['Tool'], versatility['Versatility'], color='lightcoral')
ax[1, 0].set_title('Versatility')

# Plot Time-Saving
ax[1, 1].barh(time_saving['Tool'], time_saving['Time-Saving'], color='pink')
ax[1, 1].set_title('Time-Saving')

# Adjust layout
plt.tight_layout()
plt.show()
