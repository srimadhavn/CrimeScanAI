import cv2
from ultralytics import YOLO
import tkinter as tk
from PIL import Image, ImageTk
import threading

model = YOLO("models/best.pt")  

class KnifeDetectorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Knife Detector")
        self.window.geometry("800x600")
        self.video_label = tk.Label(self.window)
        self.video_label.pack()

        self.cap = cv2.VideoCapture(0)
        self.running = True

        self.update_frame()

    def update_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if ret:
            results = model.predict(source=frame, conf=0.5, verbose=False)

            annotated_frame = results[0].plot()

            rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb)
            img = img.resize((800, 600))
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.window.after(10, self.update_frame)

    def stop(self):
        self.running = False
        self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = KnifeDetectorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.stop)
    root.mainloop()
