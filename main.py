from pulp import * #modelleme tanımlamalarını sağlayan kütüphane 

# Karar değişkenlerini tanımladım
x1 = LpVariable('x1', lowBound=0)
x2 = LpVariable('x2', lowBound=0)

#x1 ve x2 adında iki karar değişkeni tanımladım. lowBound=0, her iki değişkenin de 0'dan küçük değer alamayacağını (en az 0 olması gerektiğini) belirtiyor.

# Amaç fonksiyonu tanımladım
objective = 12*x1 + 16*x2

# Kısıtları tanımladım
problem = LpProblem('Simplex Örneği', LpMaximize) #optimizasyon yönü maximize.
problem += objective #amaç fonksiyonunu problemin bir parçası olarak ekler.
problem += 4*x1 + 5*x2 <= 40
problem += 4*x1 + 10*x2 <= 60

# Problemi çözümü
problem.solve()

# Sonuçları yazdırdım 
print("Durum:", problem.status)
print("Maksimum değer:", objective.value()) 
print("x1:", x1.value())
print("x2:", x2.value())
