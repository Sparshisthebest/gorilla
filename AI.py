import cv2
image = cv2.imread('python coding /PYgame/how to make documents/GORILAAAAAAAAAA.jpg' )
cv2.namedWindow('loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow(' Loaded Image', 500, 800)
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"image dimensions: {image.shape}")


