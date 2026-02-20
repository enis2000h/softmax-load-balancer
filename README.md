# softmax-load-balancer
# Softmax Tabanlı Yük Dengeleyici (Client-Side Load Balancer)

## 📌 Proje Amacı

Bu projede, dağıtık bir sistemde birden fazla sunucuya gelen isteklerin en verimli şekilde dağıtılması amaçlanmıştır.  
Sunucuların yanıt süreleri zamanla değiştiği ve gürültü içerdiği için klasik yük dengeleme algoritmaları (Round Robin, Random vb.) yerine öğrenebilen bir yöntem kullanılmıştır.

Bu amaçla geçmiş performans verilerine göre olasılıksal seçim yapan **Softmax Action Selection algoritması** uygulanmıştır.

Amaç:
- Ortalama gecikmeyi (latency) minimize etmek
- Toplam ödülü (reward) maksimize etmek

---

## 🧠 Kullanılan Yöntem

Bu projede problem bir **Multi-Armed Bandit** problemi olarak ele alınmıştır.

Softmax algoritması sayesinde:
- Daha iyi performans gösteren sunucuların seçilme olasılığı artar
- Ancak keşif (exploration) tamamen bırakılmaz

Böylece sistem hem öğrenir hem de dinamik ortama uyum sağlar.

---

## ⚙️ Sistem Yapısı

Proje aşağıdaki bileşenlerden oluşmaktadır:

### 1️⃣ Server (Sunucu Simülasyonu)
Her sunucu için:
- Temel gecikme süresi
- Zamana bağlı değişim (non-stationary yapı)
- Rastgele gürültü

eklenerek gerçekçi bir ortam oluşturulmuştur.

---

### 2️⃣ Softmax Load Balancer
Bu bileşen:

- Sunucu seçimini olasılıksal olarak yapar
- Her seçimden sonra ödüle göre kendini günceller
- Daha iyi sunucuların seçilme ihtimalini artırır

---

### 3️⃣ Simulation (Simülasyon Ortamı)

Simülasyon sırasında:

1. Load balancer bir sunucu seçer
2. Seçilen sunucudan gecikme alınır
3. Ödül hesaplanır → `reward = 1 / latency`
4. Algoritma kendini günceller

Bu işlem belirli adım sayısı boyunca devam eder.

---

### 4️⃣ Metrics (Performans Ölçümü)

Simülasyon sonunda:

- Ortalama gecikme
- Toplam ödül

hesaplanarak algoritmanın başarımı ölçülür.

---

## 🛠 Kullanılan Teknolojiler

- Python
- NumPy
- Matplotlib

---

## ▶️ Projeyi Çalıştırma

### 1. Gerekli kütüphaneleri kurun

```bash
pip install numpy matplotlib

