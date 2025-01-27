## Wykonaliśmy 6 wersji modelu, zmieniając funkcje straty, optymalizator oraz liczbę epok
# V1
### Funkcja straty: CrossEntropyLoss
### Optymalizator: Adam
### Liczba epok: 5
Macierz pomyłek i raport klasyfikacji:
![obraz](https://github.com/user-attachments/assets/e76f9c5a-eee8-4d1f-9389-d8f01328a01f)
![obraz](https://github.com/user-attachments/assets/7ea990f7-16bb-4c14-b827-35592d6addcc)
### Dokładność modelu: 0.91

# V2
### Funkcja straty: CrossEntropyLoss
### Optymalizator: Adam
### Liczba epok: 10
Macierz pomyłek i raport klasyfikacji:
![obraz](https://github.com/user-attachments/assets/d53184f2-6a5b-4ffa-81ff-b0217dbd14e1)
![obraz](https://github.com/user-attachments/assets/e5262d3e-4c7c-44a3-bf6d-85968ae6d306)

# V3
### Funkcja straty: NLLLoss
### Optymalizator: Adam
### Liczba epok: 5
Macierz pomyłek i raport klasyfikacji:
![obraz](https://github.com/user-attachments/assets/1dcabff9-a002-44de-aabd-66a1f3defcb7)
![obraz](https://github.com/user-attachments/assets/9006ae87-063f-490a-9698-aa8455bc3801)
### Dokładność modelu: 0.90

# V4
### Funkcja straty: NLLLoss
### Optymalizator: RMSprop
### Liczba epok: 5
Macierz pomyłek i raport klasyfikacji:
![obraz](https://github.com/user-attachments/assets/bb6a27c4-d2cc-4967-bef0-f279ef59fbe2)
![obraz](https://github.com/user-attachments/assets/bab8284c-bde0-4919-80a2-44f9b3a44802)
### Dokładność modelu: 0.91

# V5
### Funkcja straty: NLLLoss
### Optymalizator: RMSprop
### Liczba epok: 10
Macierz pomyłek i raport klasyfikacji:
![obraz](https://github.com/user-attachments/assets/f401055c-8e19-4cd5-9e12-6f65385b5ce0)
![obraz](https://github.com/user-attachments/assets/a5f37e90-ec9c-4aaa-98be-fddf261b5f37)
### Dokładność modelu: 0.91

# V6
### Funkcja straty: weighted CrossEntropyLoss
### Optymalizator: SGD
### Liczba epok: 10
Macierz pomyłek i raport klasyfikacji:
![obraz](https://github.com/user-attachments/assets/15adc445-6446-4a11-a44c-2b4b4b83fa4c)
![obraz](https://github.com/user-attachments/assets/57971aaa-84fd-412b-bec2-79ed84033ad9)
### Dokładność modelu: 0.91


# Wnioski
Przeprowadzone przez nas zmiany nie wpływają w żaden zauważalny sposób na dokładność modelu, zatem ostatecznie pozostajemy przy wersji V1, dającej najbardziej zadowalające rezultaty:
### Funkcja straty: CrossEntropyLoss
### Optymalizator: Adam
### Liczba epok: 5