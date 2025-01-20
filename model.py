import torch.nn as nn
import torch

# model sieci konwolucyjnej, dziedziczący po torch.nn.Module
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # dwie warstwy konwolucyjne
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        
        # MaxPooling zmniejsza dwukrotnie obraz dla ograniczenia parametrów i zwiększenia efektywności
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # fully connected layers
        self.fc1 = nn.Linear(32 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    # funkcja przepływu danych
    # dane przechodzą przez warstwy splotowe, max pooling, spłaszczenie danych i przez fully connected layers
    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 32 * 7 * 7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
