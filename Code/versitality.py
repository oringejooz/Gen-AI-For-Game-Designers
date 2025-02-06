import pandas as pd
import matplotlib.pyplot as plt

# Load the TSV files for each category
visual_ideation = pd.read_csv(r"Data\visual_ideation_versatility.tsv", sep='\t')
world_building = pd.read_csv(r"Data\world_building_versatility.tsv", sep='\t')
level_environment_design = pd.read_csv(r"Data\level_environment_design_versatility.tsv", sep='\t')
sound_music_ideation = pd.read_csv(r"Data\sound_music_ideation_versatility.tsv", sep='\t')
asset_creation = pd.read_csv(r"Data\asset_creation_versatility.tsv", sep='\t')

# Create a function to plot bar graphs for each category
def plot_versatility(data, category_name):
    plt.figure(figsize=(8, 6))
    plt.bar(data['Tool'], data['Versatility'], color='skyblue')
    plt.xlabel('Tool')
    plt.ylabel('Versatility')
    plt.title(f'Versatility of Tools for {category_name}')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Visualize each category
plot_versatility(visual_ideation, 'Visual Ideation')
plot_versatility(world_building, 'World Building and Narrative')
plot_versatility(level_environment_design, 'Level and Environment Design')
plot_versatility(sound_music_ideation, 'Sound and Music Ideation')
plot_versatility(asset_creation, 'Asset Creation')
