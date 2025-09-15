import cv2
import time
import pi_actuator  # actuator ko import kar rahe hain

# Load pre-trained classifier (cars.xml Haarcascade file chahiye)
car_cascade = cv2.CascadeClassifier("cars.xml")

def detect_vehicles():
    cap = cv2.VideoCapture(0)  # 0 = webcam (ya video path dal sakta hai)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 2)

        count = len(cars)
        print(f"🚗 Vehicles detected: {count}")

        # Traffic logic
        if count > 5:
            pi_actuator.control_signal("GREEN")   # Bhari traffic → green zyada
        elif 1 <= count <= 5:
            pi_actuator.control_signal("YELLOW")  # Medium traffic
        else:
            pi_actuator.control_signal("RED")     # No traffic → red

        # Show live feed
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Traffic Feed", frame)

        if cv2.waitKey(1) == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_vehicles()
   