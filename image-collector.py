import os
import time
import uuid
import cv2

IMAGES_PATH = os.path.join('data', 'images')
number_images = 90  #

images_taken = 0
auto_mode = False

cap = cv2.VideoCapture(0)
images_taken_last_value = -1

pressed_key = lambda key: cv2.waitKey(1) & 0xFF == ord(key)

while images_taken < number_images:
    if images_taken != images_taken_last_value:
        images_taken_last_value = images_taken
        print(f'[auto_mode={auto_mode}] Collecting image {images_taken + 1}/{number_images}')
    ret, frame = cap.read()
    img_name = os.path.join(IMAGES_PATH, f'{(images_taken + 1):02d}_{str(uuid.uuid1())}.jpg')
    cv2.imshow('frame', frame)

    if auto_mode or (not auto_mode and pressed_key(' ')):
        cv2.imwrite(img_name, frame)
        images_taken += 1
        time.sleep(1)
    elif pressed_key('q'):
        break
    elif pressed_key('a'):
        auto_mode = not auto_mode

# for imgnum in range(number_images):
#     print('Collecting image {}'.format(imgnum))
#     ret, frame = cap.read()
#     imgname = os.path.join(IMAGES_PATH, f'{str(uuid.uuid1())}.jpg')
#     cv2.imwrite(imgname, frame)
#     cv2.imshow('frame', frame)
#     time.sleep(0.5)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
cap.release()
cv2.destroyAllWindows()
