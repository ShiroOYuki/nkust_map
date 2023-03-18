import cv2
import numpy as np
import string

def salt_pepper_noise(image, fraction, salt_vs_pepper):
    img = np.copy(image)
    size = img.size
    num_salt = np.ceil(fraction * size * salt_vs_pepper).astype('int')
    num_pepper = np.ceil(fraction * size * (1 - salt_vs_pepper)).astype('int')
    row, column = img.shape

    x = np.random.randint(0, column - 1, num_pepper)
    y = np.random.randint(0, row - 1, num_pepper)
    img[y, x] = 0  

    x = np.random.randint(0, column - 1, num_salt)
    y = np.random.randint(0, row - 1, num_salt)
    img[y, x] = 255 
    return img

def getSlice(image_path = "verify.png"):
    image = cv2.imread(image_path)
    kernel = np.ones((4, 4), np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    image = erosion.copy()


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key=lambda x: x[1])
    ary = []
    for (c, _) in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if h>100:
            h = max(w, h)
            ary.append((x, y, h, h))

    # colorful_image= cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    for id, i in enumerate(ary):
        (x, y, w, h) = i
        # cv2.rectangle(colorful_image, (x, y), (x+w, y+h), (0, 0, 255), 10)
        roi = image[y:y+h, x:x+w]
        thresh = roi.copy()
        res = cv2.resize(thresh, (50, 50))
        cv2.imwrite(f"results/{id}.png", res)

    # cv2.imshow('image', colorful_image)
    # cv2.waitKey(0)
    
def mse(img1, img2):
    err = np.sum((img1.astype("float32") - img2.astype("float32")) ** 2)
    err /= float(img1.shape[0] * img1.shape[1])
    return err

# img1 = cv2.imread("results/0.png")
# img2 = cv2.imread("templates/30.png")
# img3 = cv2.imread("templates/24.png")
# print(mse(img1, img2))
# print(mse(img1, img3))

def getNumber(img):
    min_a = float("inf")
    result = None
    alphabetic = list(string.ascii_uppercase)
    for i in range(10):
        alphabetic.append(str(i))
    for i in range(36):
        ref = cv2.imread(f"templates/a{i}.png")
        distance = mse(img, ref)
        if distance < min_a:
            min_a = distance
            result = alphabetic[i]
    return result

def get(): 
    getSlice()
    result = ""
    for i in range(4):
        img = cv2.imread(f"results/{i}.png")
        result += getNumber(img)
    return result
    
if __name__ == "__main__":
    print(get())
        
        
