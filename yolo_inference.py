from ultralytics import YOLO

# initialize a model in the beginning
# model = YOLO("Yolov8n.pt")


# after training, load a custom model (the best model automatically saved as best.pt) now should be used

model = YOLO("models\\best.pt")

results = model.predict('input_videos\VideoFootball.mp4', save=True)

# display results for first video/frame
print(results[0])

print("***********")

for box in results[0].boxes:  
   print(box)