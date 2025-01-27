import torch.nn as nn
import torch.optim as optim
from model import CNN
from data_utils import get_data_loaders
from train_eval import train_model, test_model, evaluate_model

if __name__ == "__main__" :
    # załadowanie zbioru testowego i treningowego
    train_loader, test_loader = get_data_loaders(batch_size=64)

    # inicjalizacja modelu CNN
    model = CNN()
    criterion = nn.CrossEntropyLoss() # definicja funkcji straty
    optimizer = optim.Adam(model.parameters(), lr=0.001) # wybór optymalizatora i szybkości uczenia

    # wywołanie funkcji trenującej model
    print("Trening modelu:")
    train_model(model, train_loader, criterion, optimizer, epochs=10)

    # ocena modelu na zbiorze testowym
    print("Testowanie modelu:")
    test_model(model, test_loader)

    # tworzenie i wizualizacja macierzy pomyłek i classification report
    print("Ewaluacja modelu:")
    evaluate_model(model, test_loader)
