import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')

female_scores = df[df['gender'] == 'female'].groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()
male_scores = df[df['gender'] == 'male'].groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()

print('Средние значения оценок девочек:\n', female_scores.round(2))
print('Средние значения оценок мальчиков:\n', male_scores.round(2))

standard_scores = df[df['lunch'] == 'standard'].groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()
free_scores = df[df['lunch'] == 'free/reduced'].groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()

print('Средние значения оценок для обеда "стандарт":\n', standard_scores.round(2))
print('Средние значения оценок для бесплатного обеда:\n', free_scores.round(2))

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,8))
for i, (gender, scores) in enumerate(zip(['Девочки', 'Мальчики'], [female_scores, male_scores])):
    for j, (subject, color) in enumerate(zip(['math score', 'reading score', 'writing score'], ['r', 'g', 'b'])):
        ax = scores[subject].plot(kind='barh', color=color, ax=axes[i,j])
        ax.set_xlabel(subject)
        ax.set_ylabel('Уровень образования родителей')
        ax.set_title('{} - {} scores'.format(gender.capitalize(), subject.capitalize()))

plt.tight_layout()
plt.show()
