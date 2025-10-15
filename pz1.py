import pandas as pd
url = "https://drive.google.com/uc?export=download&id=1MVbh3ReFZEw3uKreAj2s0ftYiUHvT0qa"
df = pd.read_csv(url)
print(df.head())
df['co'] = df['co'] * 1000
print(df.head())
light_true_df = df[df['light'] == True].copy()
output_filename = 'light_on.csv'
light_true_df.to_csv(output_filename, index=False)
print({output_filename})
print("Первые 5 строк нового файла:")
print(light_true_df.head())
processed_df = pd.read_csv(output_filename)
processed_df['formatted_time'] = pd.to_datetime(processed_df['ts'], unit='s').dt.strftime('%Y-%m-%d %H:%M')
processed_df.to_csv(output_filename, index=False)
print({output_filename})
print(processed_df.head())