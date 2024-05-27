import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from sklearn.metrics import f1_score, confusion_matrix
from preprocess_data import prepare_data_loader

# 모델 정의
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 32 * 32, 512)
        self.fc2 = nn.Linear(512, 6)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 32 * 32)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 모델 인스턴스 생성 및 가중치 로드
model = SimpleCNN()
model.load_state_dict(torch.load('model.pth'))  # 'model.pth' 파일에서 모델의 가중치 로드
model.eval()  # 모델을 평가 모드로 설정

# 데이터셋과 DataLoader 설정
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 가정: `test_loader`가 이미 정의되어 있거나, 여기에 대한 정의가 필요합니다.
# 예시: test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# 테스트 루프 정의 및 실행
def test_model(model, test_loader):
    model.eval()
    all_predicted = []
    all_labels = []
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            all_predicted.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    f1_scores = f1_score(all_labels, all_predicted, average=None)
    cm = confusion_matrix(all_labels, all_predicted)
    class_accuracy = 100 * cm.diagonal() / cm.sum(axis=1)

    print("Performance per class:")
    for i, (acc, f1) in enumerate(zip(class_accuracy, f1_scores)):
        print(f'Class {i}: Accuracy: {acc:.2f}%, F1 Score: {f1:.4f}')

def evaluate_model():
    folder_path = "../test1"
    batch_size = 32
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # DataLoader 준비
    test_loader = prepare_data_loader(folder_path, transform, batch_size)

    # 모델 인스턴스 생성 및 가중치 로드
    model = SimpleCNN()
    model.load_state_dict(torch.load('model.pth'))  # 모델 가중치 파일
    model.eval()

    # 모델 테스트
    test_model(model, test_loader)

if __name__ == "__main__":
    evaluate_model()