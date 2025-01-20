from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# przygotowanie danych
# pobranie zbioru FashionMNIST, przekształcenie go do odpowiedniego formatu
# podział na zbiór testowy i treningowy
def get_data_loaders(batch_size=64):
    # konwersja obrazów na tensory pytorch i normalizacja
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # pobranie zbiorów testowych i treningoywch do katalogu ./data
    train_dataset = datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)

    # tworzenie dataloaderów
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader
