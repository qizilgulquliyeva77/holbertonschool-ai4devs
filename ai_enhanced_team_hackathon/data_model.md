# Data Model

Sistem, aşağıdaki üç ana varlık (entity) ve aralarındaki ilişkiler üzerine kuruludur:

### 1. User (Kullanıcı)
*   **ID:** UUID (Primary Key)
*   **FullName:** String
*   **Email:** String (Unique)
*   **PasswordHash:** String
*   **CreatedAt:** DateTime

### 2. Product (Ürün)
*   **ID:** UUID (Primary Key)
*   **Name:** String
*   **Description:** Text
*   **Price:** Decimal
*   **StockQuantity:** Integer
*   **CategoryID:** FK (Category Entity)

### 3. Order (Sipariş)
*   **ID:** UUID (Primary Key)
*   **UserID:** FK (User.ID)
*   **TotalPrice:** Decimal
*   **Status:** Enum (Pending, Shipped, Delivered, Cancelled)
*   **OrderDate:** DateTime

---
**İlişkiler:**
- Bir **User** birden fazla **Order** verebilir (1:N).
- Bir **Order** birden fazla **Product** içerebilir (N:M - *OrderItems ara tablosu ile*).
