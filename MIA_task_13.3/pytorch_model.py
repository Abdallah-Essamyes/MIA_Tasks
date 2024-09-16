import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define the neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Input layer  pixels
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 64)
        # Output layer digits 0-9
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        # Flatten the image
        x = x.view(-1, 28 * 28)
        # ReLU activation
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Loading the MNIST dataset
def load_data(batch_size=64):
    # Transformation (normalize values between -1 and 1)
    transform = transforms.Compose([transforms.ToTensor(),
                                    transforms.Normalize((0.5,), (0.5,))])

    # Load MNIST dataset
    train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

    # Data loaders
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader

# Train the model
def train_model(net, train_loader, optimizer, criterion, epochs=5):
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            # Zero the parameter gradients
            optimizer.zero_grad()

            # Forward pass
            outputs = net(images)
            loss = criterion(outputs, labels)

            # Backward pass and optimization
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader)}")

# Test the model
def test_model(net, test_loader):
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f"Accuracy: {100 * correct / total}%")

# Main function
def main():
    # Hyperparameters
    learning_rate = 0.003
    epochs = 5
    batch_size = 64

    # Load data
    train_loader, test_loader = load_data(batch_size)

    # Initialize network, loss function and optimizer
    net = Net()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=learning_rate)

    # Train the network
    train_model(net, train_loader, optimizer, criterion, epochs)

    # Test the network
    test_model(net, test_loader)

if __name__ == '__main__':
    main()