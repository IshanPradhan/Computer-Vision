import cv2
import time

video = cv2.VideoCapture(0)

frame_rate = 1

first_frame = None

while True:
    check, frame = video.read()
    # status = 0

    frame_rate = frame_rate + 1
    # print(check)
    # print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # delta_frame = cv2.absdiff(first_frame, gray)

    # time.sleep(3)

    # thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # thresh_delta = cv2.dilate(thresh_delta, None, iterations=2)

    # (_, cnts, _) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    """for countour in cnts:
        if cv2.contourArea(countour) < 1000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+h, y+w), (0, 0, 255), 3)
    """

    cv2.imshow("Capturing", gray)
    # cv2.imshow("Delta Frame", delta_frame)
    # cv2.imshow("Threshold Frame", thresh_delta)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

    # print(status)


# print(frame_rate)
video.release()

cv2.destroyAllWindows()
