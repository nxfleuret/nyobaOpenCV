import cv2

# # how to read an image and save it in to variable/s
# # 1 = colored image
# # 0 = grayscale image
# # -1 = unchanged image with the alpha channel
# imgLena = cv2.imread('lena.jpg', -1)

# # print image's in matrix form
# print(imgLena)

# # to show the image
# cv2.imshow('image', imgLena)
# # time (in milisec) for the image window to be opened (0 means window will open until we make an action)
# key = cv2.waitKey(0) & 0xFF

# # if we press 'esc' key wich was numbered as '27', the window will be closed and if we press 's' key, the image will be copied as the chosen name and format written on the argument
# if key == 27:
#     cv2.destroyAllWindows()
# elif key == ord('s'):
#     # to copy an image
#     cv2.imwrite('lenaCopy.png', imgLena)
#     cv2.destroyAllWindows()

# to initiate the video capturing method, the number is your camera (0 mean default camera), the argument can also be filled with video file name
capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = capture.read()

    if ret == True:
        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        output.write(frame)

        # to make the video capture in grayscale mode
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()

