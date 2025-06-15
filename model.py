from ultralytics import YOLO

model = YOLO('yolov8s.pt')  

results = model.train(
    data='data.yaml',
    lr0=0.01,
    batch=8,
    epochs=35,           
    name='detected',
    workers=0,
    imgsz=640,
    patience = 10           
)