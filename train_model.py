import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from joblib import dump

# 1. Veriyi oku
url = "https://raw.githubusercontent.com/erkansirin78/datasets/master/Advertising.csv"
df = pd.read_csv(url)

# 2. Özellikler (TV, Radio, Newspaper) ve hedef değişken (Sales)
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# 3. Eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 4. Modeli eğit
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Tahmin yap ve R2 skorunu hesapla
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"Model başarı skoru (R²): {r2:.4f}")

# 6. Modeli kaydet
dump(model, 'advertising_model.pkl')
print("Model kaydedildi: advertising_model.pkl")