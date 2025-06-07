from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

# 1. Modeli yükle
model = load('advertising_model.pkl')

# 2. FastAPI uygulamasını başlat
app = FastAPI()

# 3. Girdi (input) veri sınıfı
class AdvertisingData(BaseModel):
    TV: float
    Radio: float
    Newspaper: float

# 4. Çıktı (output) veri sınıfı
class SalesPrediction(BaseModel):
    Sales: float

# 5. Tahmin endpoint'i
@app.post("/prediction/advertising", response_model=SalesPrediction)
def predict_advertising(data: AdvertisingData):
    # Girdileri modele uygun hale getir
    features = [[data.TV, data.Radio, data.Newspaper]]
    
    # Tahmin yap
    prediction = model.predict(features)[0]
    
    # Sonucu döndür
    return SalesPrediction(Sales=prediction)