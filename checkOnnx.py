import onnx
import onnxruntime as ort
import numpy as np

# ==============================
# Cargar modelo ONNX
# ==============================
ONNX_PATH = "best.onnx"
CLASSES_PATH = "classes.txt"

# Leer clases
with open(CLASSES_PATH, "r") as f:
    classes = [line.strip() for line in f.readlines()]
num_classes = len(classes)
expected_size = 5 + num_classes  # x,y,w,h,conf + num_classes

# ==============================
# Preparar sesión ONNX Runtime
# ==============================
session = ort.InferenceSession(ONNX_PATH)

# Obtener nombre de input
input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape
print(f"Input name: {input_name}, shape: {input_shape}")

# Crear dummy input (batch 1)
dummy_input = np.random.rand(*[dim if dim is not None else 1 for dim in input_shape]).astype(np.float32)

# Inferencia dummy
outputs = session.run(None, {input_name: dummy_input})
print(f"Output shape(s): {[o.shape for o in outputs]}")

# Calcular número de boxes
trt_output_size = np.prod(outputs[0].shape)
num_boxes = trt_output_size // expected_size
print(f"Salida total: {trt_output_size}, expected_size por box: {expected_size}")
print(f"Número de cajas (num_boxes): {num_boxes}")
