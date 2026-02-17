from ultralytics import YOLO
import torch

def train():

    device = 0 if torch.cuda.is_available() else "cpu"

    model = YOLO("yolov5s.pt")  # sigue usando arquitectura v5 si quieres

    model.train(
        data="D:/UpgradeKnowC_Python/PythonUpgrade/project-3/data.yaml",
        epochs=80,
        imgsz=640,
        batch=16,
        device=device,
        project="DeteccionContenedores",
        name="entrenamiento_local"
    )

if __name__ == "__main__":
    train()
