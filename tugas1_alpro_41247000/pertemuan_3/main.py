import pandas as pd

# 1. Buat dataframe
data = {
    'Nama': ['Galang', 'Indra', 'Yudis', 'Syaiful', 'Subri'],
    'Tinggi_Badan': [170, 160, 175, 165, 170],  # dalam cm
    'Umur': [25, 22, 27, 21, 19],  # dalam tahun
    'Berat_Badan': [70, 50, 80, 55, 60]  # dalam kg
}

df = pd.DataFrame(data)

# 2. Simpan ke dalam file CSV
csv_file = 'data_kelompok.csv'
df.to_csv(csv_file, index=False)
print(f"Data berhasil disimpan dalam file: {csv_file}")

# 3. Baca file CSV dan lakukan manipulasi data
df = pd.read_csv(csv_file)

# Manipulasi 1: Tambahkan kolom BMI (Body Mass Index)
df['bmi'] = df['berat_badan'] / ((df['tinggi_badan'] / 100) ** 2)

# Manipulasi 2: Urutkan data berdasarkan umur
df = df.sort_values(by='umur')

# Manipulasi 3: Filter data dengan BMI > 22
filtered_df = df[df['bmi'] > 22]

# Manipulasi 4: Ubah nama kolom menjadi lowercase (sudah diatasi sebelumnya)

print("\nData setelah manipulasi:")
print(df)
