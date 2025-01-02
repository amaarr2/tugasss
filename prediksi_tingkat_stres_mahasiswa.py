# -*- coding: utf-8 -*-
"""PREDIKSI TINGKAT STRESS MAHASISWA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LW2Wzg3kDuJTNXm49zTVVpi4zsxziW0w

**PREDIKSI TINGKAT STRESS MAHASISWA DENGAN ANALISIS DATA POLA HIDUP HARIAN**
"""

uploaded = files.upload()

import pandas as pd

# Load dataset
data = pd.read_csv('student_lifestyle_dataset.csv')

# Tampilkan beberapa baris pertama untuk memastikan dataset berhasil dimuat
data.head()

# Informasi dataset
data.info()

# Statistik deskriptif untuk kolom numerik
data.describe()

# Distribusi tingkat stres
print(data['Stress_Level'].value_counts())

import matplotlib.pyplot as plt
import seaborn as sns

# Distribusi tingkat stres
sns.countplot(data=data, x='Stress_Level', palette='viridis')
plt.title("Distribusi Tingkat Stres Mahasiswa")
plt.show()

# Heatmap korelasi
numerical_columns = [
    'Study_Hours_Per_Day', 'Extracurricular_Hours_Per_Day',
    'Sleep_Hours_Per_Day', 'Social_Hours_Per_Day',
    'Physical_Activity_Hours_Per_Day', 'GPA'
]
sns.heatmap(data[numerical_columns].corr(), annot=True, cmap='coolwarm')
plt.title("Korelasi Antar Fitur")
plt.show()

from sklearn.preprocessing import LabelEncoder

# Encode Stress_Level ke numerik
label_encoder = LabelEncoder()
data['Stress_Level_Encoded'] = label_encoder.fit_transform(data['Stress_Level'])
print(label_encoder.classes_)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numerical_columns = [
    'Study_Hours_Per_Day', 'Extracurricular_Hours_Per_Day',
    'Sleep_Hours_Per_Day', 'Social_Hours_Per_Day',
    'Physical_Activity_Hours_Per_Day', 'GPA'
]
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

from sklearn.model_selection import train_test_split

# Fitur (X) dan target (y)
X = data[numerical_columns]
y = data['Stress_Level_Encoded']

# Membagi data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Inisialisasi dan latih model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi Model:", accuracy)

from sklearn.metrics import classification_report, confusion_matrix

# Laporan klasifikasi
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title("Confusion Matrix")
plt.xlabel("Prediksi")
plt.ylabel("Aktual")
plt.show()