# High-Level Architecture Plan

Sistem, ölçeklenebilirlik ve bakım kolaylığı için **Client-Server** mimarisine dayalı bir yapıda tasarlanmıştır.

### 1. Frontend (Sunum Katmanı)
*   **Teknoloji:** React.js veya Next.js.
*   **Sorumluluk:** Kullanıcı arayüzünü sağlamak, API isteklerini yönetmek ve state (durum) yönetimi.

### 2. Backend (Uygulama Katmanı)
*   **Teknoloji:** Node.js (Express) veya Python (FastAPI).
*   **Mimari:** RESTful API.
*   **Sorumluluk:** İş mantığının (business logic) yürütülmesi, kimlik doğrulama (JWT), veritabanı CRUD işlemleri ve güvenlik.

### 3. Database (Veri Katmanı)
*   **Teknoloji:** PostgreSQL (İlişkisel veriler için).
*   **Sorumluluk:** Kullanıcı, ürün ve sipariş verilerinin tutarlı bir şekilde saklanması.

### 4. Entegrasyonlar ve Altyapı
*   **Ödeme Sistemi:** Iyzico veya Stripe API entegrasyonu.
*   **Barındırma:** Dockerize edilmiş konteynerler kullanılarak AWS veya Google Cloud üzerinde dağıtım.
*   **Caching:** Performans için Redis kullanımı planlanmaktadır.
