import cv2 
import numpy as np 
import skimage.exposure

video = cv2.VideoCapture("../Assets/green_image.mp4")
image = cv2.imread("../Assets/white-background.jpg")

fps = int(video.get(cv2.CAP_PROP_FPS))
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or 'XVID' or 'MJPG'
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (frame_width, frame_height))


while True:


    ret, img = video.read()

    if(ret == False):
        break

    lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

    A = lab[:,:,1]

    thresh = cv2.threshold(A, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

    blur = cv2.GaussianBlur(thresh, (0,0), sigmaX=5, sigmaY=5, borderType = cv2.BORDER_DEFAULT)

    mask = skimage.exposure.rescale_intensity(blur, in_range=(127.5,255), out_range=(0,255)).astype(np.uint8)
    # cv2.imshow('mask', mask)
    result = img.copy()
    result = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)

    result[:,:,3] = mask

    result[result[:, :, 3] == 0] = [255, 255, 255, 255]


    # print(type(result), result.shape , type(mask), mask.shape)

    out.write(result)

    cv2.imshow('Input : ', img)
    cv2.imshow('Output: ', result)

    if cv2.waitKey(25) == 27:
        break 
    
    

video.release()
cv2.destroyAllWindows()
