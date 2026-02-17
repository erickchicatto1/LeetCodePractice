from ultralytics import YOLO

model = YOLO("D:/UpgradeKnowC_Python/PythonUpgrade/project-3/DeteccionContenedores/entrenamiento_local2/weights/best.pt")


model.export(
    format="onnx",
    opset=12,
    dynamic=True
)
