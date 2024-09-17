from PIL import Image
from ultralytics import YOLO

model = YOLO("yolov8l.pt")

def check_border_touch(image_width, image_height, cords):
    x_min, y_min, x_max, y_max = cords
    if x_min <= 0 or y_min <= 0 or x_max >= image_width or y_max >= image_height:
        print("The whole car is not visible. Make sure you are not too close to the car and the whole car is being captured.")
    else:
        print("Car is captured properly. Not touching border.")

def calculate_area(image_width, image_height, cords):
    x_min, y_min, x_max, y_max = cords
    car_area = (x_max - x_min) * (y_max - y_min)
    image_area = image_width * image_height
    return car_area / image_area

def check_camera_distance(image_width, image_height, cords):
    car_coverage = calculate_area(image_width, image_height, cords)
    if car_coverage < 1/3:
        print("It seems you are too far from the car. Get close.")
    else:
        print("Car distance is optimal.")
        check_border_touch(image_width, image_height, cords)

image_path = "./sample_data/car.jpg"
image = Image.open(image_path)
image = image.resize((640, 320))
results = model.predict(source=image, imgsz=(640), classes=2,
                        show=True, save=True, show_conf=True)

try:
    box = results[0].boxes[0]
    cords = box.xyxy[0].tolist()
    cords = [round(x) for x in cords]
    conf = round(box.conf[0].item(), 2)
    print("---")
    print("Coordinates:", cords)
    print("Probability:", conf)
    print("---")

    check_camera_distance(image.width, image.height, cords)
except IndexError:
    print("Sorry, we can not detect any car.")
