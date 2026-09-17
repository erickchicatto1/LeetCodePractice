import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulate a Regolith Sample Dataset (Grains measured in micrometers)
# Planetary regolith contains a mix of fine dust and larger rock fragments
np.random.seed(42)
fine_dust = np.random.normal(loc=20, scale=8, size=1500)      # Fine particles (e.g., 20 µm)
coarse_grains = np.random.normal(loc=150, scale=40, size=500)  # Larger grains (e.g., 150 µm)
all_particles = np.concatenate([fine_dust, coarse_grains])
all_particles = all_particles[all_particles > 0]  # Remove unphysical negative sizes

# Store measurements in a Pandas DataFrame
df = pd.DataFrame(all_particles, columns=['Particle_Size_Um'])

# 2. Statistical Analysis of the Regolith Sample
print("--- LUNAR REGOLITH SAMPLE METRICS ---")
print(f"Total Particles Measured: {len(df)}")
print(f"Mean Particle Size       : {df['Particle_Size_Um'].mean():.2f} µm")
print(f"Median Particle Size (D50): {df['Particle_Size_Um'].median():.2f} µm")
print(f"Minimum Size Detected    : {df['Particle_Size_Um'].min():.2f} µm")
print(f"Maximum Size Detected    : {df['Particle_Size_Um'].max():.2f} µm")

# Calculate D10, D50, D90 metrics (standard for soil/regolith analysis)
d10 = np.percentile(df['Particle_Size_Um'], 10)
d90 = np.percentile(df['Particle_Size_Um'], 90)
print(f"D10 (10% are smaller than): {d10:.2f} µm")
print(f"D90 (90% are smaller than): {d90:.2f} µm")

# 3. Visualization: Particle Size Distribution Plot
plt.figure(figsize=(10, 5))

# Plot Histogram (Frequency)
plt.hist(df['Particle_Size_Um'], bins=50, color='slategray', edgecolor='black', alpha=0.7, label='Particle Count')

# Formatting the Chart
plt.title('Planetary Regolith Particle Size Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Particle Diameter (micrometers - µm)', fontsize=12)
plt.ylabel('Frequency / Count', fontsize=12)
plt.axvline(df['Particle_Size_Um'].median(), color='red', linestyle='--', linewidth=2, label=f'D50 Median ({df["Particle_Size_Um"].median():.1f} µm)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Display the output
plt.tight_layout()
plt.show()
