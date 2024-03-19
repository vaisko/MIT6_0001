import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# CSV data as a string
csv_data = """
Pill,Experience,Strength,Effectiveness
regular_mdma_pill,regular,-0.04,0.98
strong_mdma_pill,regular,1.75,0.99
monster_dose_mdma_pill,regular,3.07,0.99
weak_mdma_pill,regular,-2.05,0.35
treshold_mdma_pill,regular,-1,0
regular_mdma_w_regular_amp_pill,semi_experienced,1.4,0.84
regular_mdma_w_trace_amp_pill,semi_experienced,-0.04,0.98
regular_3_mmc_pill,semi_experienced,0.14,0.77
strong_3_mmc_pill,semi_experienced,3.98,0.72
mdma_w_meth_pill,semi_experienced,2.38,0.75
amphetamine_only_pill,semi_experienced,0.39,0.33
caffeine_only_pill,semi_experienced,-1.4,0
strong_caffeine_pill,semi_experienced,-0.27,0
caffeine_w_meth_pill,semi_experienced,5.5,0.17
fucked_up_pill,semi_experienced,3.84,0.38
fucked_up_w_mdma_pill,semi_experienced,7.79,0.37
regular_mdma_pill,less_experienced,0.22,0.97
strong_mdma_pill,less_experienced,2.09,0.97
monster_dose_mdma_pill,less_experienced,3.42,0.97
weak_mdma_pill,less_experienced,-1.73,0.56
treshold_mdma_pill,less_experienced,-1,0
regular_mdma_w_regular_amp_pill,less_experienced,1.51,0.84
regular_mdma_w_trace_amp_pill,less_experienced,0.22,0.97
regular_3_mmc_pill,less_experienced,0.13,0.75
strong_3_mmc_pill,less_experienced,4.07,0.75
mdma_w_meth_pill,less_experienced,2.65,0.75
amphetamine_only_pill,less_experienced,0.39,0.43
caffeine_only_pill,less_experienced,-0.84,0
strong_caffeine_pill,less_experienced,-0.16,0
caffeine_w_meth_pill,less_experienced,5.82,0.14
fucked_up_pill,less_experienced,4.04,0.36
fucked_up_w_mdma_pill,less_experienced,8.26,0.36
regular_mdma_pill,inexperienced,-0.01,1
strong_mdma_pill,inexperienced,2.09,1
monster_dose_mdma_pill,inexperienced,3.47,1
weak_mdma_pill,inexperienced,-1.8,0.49
treshold_mdma_pill,inexperienced,-1,0
regular_mdma_w_regular_amp_pill,inexperienced,1.27,0.74
regular_mdma_w_trace_amp_pill,inexperienced,-0.01,1
regular_3_mmc_pill,inexperienced,0.07,0.84
strong_3_mmc_pill,inexperienced,3.91,0.56
mdma_w_meth_pill,inexperienced,2.56,0.66
amphetamine_only_pill,inexperienced,0.5,0.19
caffeine_only_pill,inexperienced,-0.89,0.01
strong_caffeine_pill,inexperienced,-0.02,0
caffeine_w_meth_pill,inexperienced,6.49,0.09
fucked_up_pill,inexperienced,3.9,0.33
fucked_up_w_mdma_pill,inexperienced,8.96,0.23
regular_mdma_pill,least_experienced,-0,0.84
strong_mdma_pill,least_experienced,1.84,0.85
monster_dose_mdma_pill,least_experienced,3.01,0.85
weak_mdma_pill,least_experienced,-1.63,0.14
treshold_mdma_pill,least_experienced,-1,0
regular_mdma_w_regular_amp_pill,least_experienced,0.58,0.84
regular_mdma_w_trace_amp_pill,least_experienced,-0,0.84
regular_3_mmc_pill,least_experienced,-0.26,0.78
strong_3_mmc_pill,least_experienced,2.97,0.84
mdma_w_meth_pill,least_experienced,1.91,0.84
amphetamine_only_pill,least_experienced,-0.49,0.59
caffeine_only_pill,least_experienced,-1,0
strong_caffeine_pill,least_experienced,-0.39,0
caffeine_w_meth_pill,least_experienced,4.24,0.39
fucked_up_pill,least_experienced,2.66,0.61
fucked_up_w_mdma_pill,least_experienced,6.32,0.74
regular_mdma_pill,no_experience,0,0.91
strong_mdma_pill,no_experience,1.13,0.91
monster_dose_mdma_pill,no_experience,2.29,0.91
weak_mdma_pill,no_experience,-1.56,0.21
treshold_mdma_pill,no_experience,-0.86,0.05
regular_mdma_w_regular_amp_pill,no_experience,0.1,0.91
regular_mdma_w_trace_amp_pill,no_experience,0,0.91
regular_3_mmc_pill,no_experience,-0.45,0.8
strong_3_mmc_pill,no_experience,2.44,0.91
mdma_w_meth_pill,no_experience,1.42,0.91
amphetamine_only_pill,no_experience,-0.88,0.44
caffeine_only_pill,no_experience,-0.86,0.05
strong_caffeine_pill,no_experience,-0.49,0
caffeine_w_meth_pill,no_experience,3.44,0.37
fucked_up_pill,no_experience,2.24,0.74
fucked_up_w_mdma_pill,no_experience,4.87,0.65
"""

# Create a DataFrame from CSV data
df = pd.read_csv(StringIO(csv_data))

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Strength'], df['Effectiveness'], c=df['Experience'].astype('category').cat.codes, cmap='viridis', s=100)

# Add labels and title
plt.title('Pill Effectiveness vs Strength')
plt.xlabel('Strength')
plt.ylabel('Effectiveness')

# Add legend
legend_labels = df['Experience'].unique()
plt.legend(legend_labels, loc='upper right')

# Show the plot
plt.show()
