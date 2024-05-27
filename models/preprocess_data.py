import os
import cv2
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

# 이미지 분류 함수
def classify_image(width_ratio, height_ratio, relative_x_position, distance_from_top, distance_from_bottom):
    if height_ratio < 0.3:
        return 1  # Small_Figure
    elif height_ratio > 0.7:
        return 2  # Large_Figure
    elif distance_from_bottom > 0.3:
        return 3  # Excessive_Floor
    elif distance_from_bottom < 0.01:
        return 4  # Limited_Floor
    elif relative_x_position < 0.3 or relative_x_position > 0.7:
        return 5  # Off_Center_Figure
    else:
        return 0  # Full_Body_Visible

# YOLO 모델 로드
def load_yolo_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

# 사용자 정의 데이터셋 클래스
class CustomImageDataset(Dataset):
    def __init__(self, img_labels, folder_path, transform=None):
        self.img_labels = img_labels
        self.folder_path = folder_path
        self.transform = transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path, label = self.img_labels[idx]
        img_path = os.path.join(self.folder_path, img_path)

        image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        if image is None:
            raise FileNotFoundError(f"The image at path {img_path} could not be loaded.")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)

        if self.transform:
            image = self.transform(image)

        return image, label

# 이미지 처리 및 분류 결과 생성
def process_images(folder_path):
    model = load_yolo_model()
    classification_results = []

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(folder_path, file_name)
            img = cv2.imread(file_path)
            if img is None:
                continue
            height, width, _ = img.shape

            results = model(img)
            max_conf = 0
            best_det = None
            for *xyxy, conf, cls in results.xyxy[0]:
                if conf > max_conf:
                    max_conf = conf
                    best_det = (*xyxy, conf, cls)

            if best_det:
                x1, y1, x2, y2, conf, cls = best_det
                width_ratio = (x2 - x1) / width
                height_ratio = (y2 - y1) / height
                relative_x_position = (x1 + x2) / (2 * width)
                distance_from_top = y1 / height
                distance_from_bottom = 1 - (y2 / height)

                classification = classify_image(width_ratio, height_ratio, relative_x_position, distance_from_top, distance_from_bottom)
                classification_results.append((file_name, classification))

    return classification_results

# 데이터 로더 준비
def prepare_data_loader(folder_path, transform, batch_size=32):
    classification_results = process_images(folder_path)
    dataset = CustomImageDataset(classification_results, folder_path, transform)

    # 테스트용 데이터 로더 생성
    test_loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    return test_loader

if __name__ == "__main__":
    folder_path = "../test1"
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    test_loader = prepare_data_loader(folder_path, transform)
