from PIL import Image
from ultralytics import YOLO

model = YOLO("yolov8l.pt")

image = "/content/car_right.jpg"
image = Image.open(image)
image = image.resize((640, 320))
results = model.predict(source = image, imgsz=(640), classes=2,
                               show=True, save=True, show_conf=True,
)

box = results[0].boxes[0]
cords = box.xyxy[0].tolist()
cords = [round(x) for x in cords]
conf = round(box.conf[0].item(), 2)

print("---")
print("Coordinates:", cords)
print("Probability:", conf)
print("---")

def check_border_touch(image_width, image_height, cords):
    x_min, y_min, x_max, y_max = cords
    if x_min <= 0 or y_min <= 0 or x_max >= image_width or y_max >= image_height:
        print("The whole car is not visible. Make sure you are not too close to the car and the whole car is being captured.")
    else:
        print("Processing")

check_border_touch(640, 320, cords)
