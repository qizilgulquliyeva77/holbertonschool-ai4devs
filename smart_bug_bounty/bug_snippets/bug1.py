def calculate_average(numbers):
    # Hata Düzeltildi: Sum 0'dan başlamalı
    # Pythonic Yaklaşım: 'sum()' fonksiyonu döngüden daha hızlı ve temizdir.
    
    if not numbers:
        # Hata Düzeltildi: Liste boşsa ZeroDivisionError'ı önlemek için kontrol
        return 0 # Boş bir liste için ortalama 0 diyebiliriz veya 'None' dönebiliriz.
        # Ya da bir hata fırlatabiliriz: raise ValueError("Liste boş olamaz.")
        
    total_sum = sum(numbers) 
    return total_sum / len(numbers)

# Testler
data_empty = []
data_with_values = [10, 20, 30, 40, 50]
data_with_one = [100]

print(f"Boş liste ortalaması: {calculate_average(data_empty)}")
print(f"Dolu liste ortalaması: {calculate_average(data_with_values)}")
print(f"Tek elemanlı liste ortalaması: {calculate_average(data_with_one)}")
