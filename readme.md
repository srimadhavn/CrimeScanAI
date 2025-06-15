
# Weapon Detection 

A real-time object detection system fine-tuning **YOLOv8** base model with custom Datasets that helps in identifying **handguns** and **knives** from a live webcam feed. This project is ideal for security systems, surveillance, and public safety applications.

### Run the app:

```bash
python webcam.py
```

This opens a Tkinter-based window that streams your webcam with live annotations for detected guns and knives.

---

## Model Info

- **Framework**: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- **Classes**: Handgun, Knife
- **mAP@0.5**: `0.887`
- **mAP@0.5:0.95**: `0.632`
- **F1-Score**: `0.8090`


---

## Training

### To retrain the model:

```python
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
model.train(data="data.yaml", epochs=35, imgsz=640)
```

`data.yaml` should look like this:

```yaml
train: train/images
val: valid/images
test: test/images
nc: 2
names: ['Handgun', 'Knife']
```

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Model Weights

The trained model is stored in:

```
models/best.pt
```

If it’s missing, [download it here](https://drive.google.com/file/d/10la4EtoviR7jjnWsl9dtkc4RM2C6VTIo/) (or train it again).

---

## Use Cases

This model can be integrated into:
- Airport or metro surveillance systems
- Smart CCTV setups
- Restricted area security alerts
- Real-time alert systems for schools or malls

---
