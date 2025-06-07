# 📦 Advertising Model Deployment with FastAPI, Docker, and Terraform

## 🎯 Amaç
Bu proje, bir makine öğrenmesi modelini FastAPI ile REST API olarak sunmayı, Docker ile containerize etmeyi ve Terraform ile dağıtım altyapısını otomatikleştirmeyi amaçlar. Model, reklam bütçelerine göre satış tahmini yapmaktadır.

---

## 🔍 Problem Tanımı

### 🧠 1. Model Eğitimi
- Kullanılan veri seti: [Advertising.csv](https://raw.githubusercontent.com/erkansirin78/datasets/master/Advertising.csv)
- Model: `RandomForestRegressor`
- Girdi: `TV`, `Radio`, `Newspaper`
- Çıktı: `Sales`
- Kaydedilen model: `advertising_model.pkl`

### ⚙️ 2. FastAPI Uygulaması
- Endpoint: `POST /prediction/advertising`
- Girdi (JSON):
  ```json
  {
    "TV": 230.1,
    "Radio": 37.8,
    "Newspaper": 69.2
  }
Çıktı (JSON):

{
  "prediction": 22.5
}
🐳 3. Docker Container
FastAPI uygulaması containerize edildi.

Dockerfile ile 8000 portu expose edildi.

🌍 4. Terraform ile Dağıtım
Docker imajı oluşturuluyor.

Docker container başlatılıyor.

Port yönlendirmesi: 8002 (host) ➝ 8000 (container)

🚀 Projeyi Çalıştırmak
1. Modeli Eğit
python train_model.py
2. Docker ve Terraform ile Dağıtım
terraform init
terraform apply
3. API'yi Test Et
Swagger UI: http://localhost:8002/docs

Örnek test verisi:

json

{
  "TV": 230.1,
  "Radio": 37.8,
  "Newspaper": 69.2
}
🗂️ Proje Dosya Yapısı
.
├── advertising_model.pkl
├── Dockerfile
├── main.py
├── main.tf
├── requirements.txt
├── terraform.tfstate
├── terraform.tfstate.backup
├── train_model.py
└── .terraform/
🛠️ Kullanılan Teknolojiler
Python

FastAPI

Docker

Terraform

scikit-learn

Pydantic

👤 Geliştirici
Bu proje MLOps Bootcamp kapsamında hazırlanmıştır.



### ✅ Sonraki Adım:
Bu içeriği `README.md` dosyana yapıştır → kaydet → sonra terminalde şunları çalıştır:

```bash
echo ".terraform/" >> .gitignore
git add .
git commit -m "Add README and ignore .terraform"
git push origin main