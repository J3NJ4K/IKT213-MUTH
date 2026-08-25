import cv2

cam = cv2.VideoCapture(0)

fps = int(cam.get(cv2.CAP_PROP_FPS))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))

with open("camera_outputs.txt", "w") as f:
    f.write(f"fps : {fps}\n")
    f.write(f"height : {frame_height}\n")
    f.write(f"width : {frame_width}\n")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()