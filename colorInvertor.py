import numpy as np
import cv2 as cv
import os

GIVEN_IMAGE=os.environ.get("IMAGE_LOC")
given=str(GIVEN_IMAGE)
OUTPUT_FILE=str(given[:len(given)-4])

if __name__ == '__main__':
    def Image_Inversion(Image):
        Height=Image.shape[0]
        Width=Image.shape[1]
        Channels=Image.shape[2]

        Size=(Height, Width, Channels)
        New_image=np.zeros(Size, np.uint8)

        for i in range(Height):
            for j in range(Width):
                for k in range(Channels):
                    New_image[i,j,k]=255-Image[i,j,k]
        return New_image

    input_img=cv.imread(f"{GIVEN_IMAGE}")
    result=Image_Inversion(input_img)
    cv.imwrite(f".\inverted\{OUTPUT_FILE}_inverted.png",result)