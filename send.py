import argparse
import time

import cv2


def stream_video(ip, port):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(f"udp://{ip}:{port}")

    while True:
        # Read frame
        ret, frame = cap.read()

        # If frame is not read correctly, ret is False
        if not ret:
            print("Can't receive frame (stream end?). Retrying in 1 second ...")
            time.sleep(1)
            continue

        # Display the resulting frame
        cv2.imshow("UDP Video Stream", frame)

        # Press 'q' on keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Receive UDP video stream.")
    parser.add_argument(
        "--ip", type=str, required=True, help="IP address for UDP video stream."
    )
    parser.add_argument(
        "--port", type=int, required=True, help="Port number for UDP video stream."
    )

    args = parser.parse_args()

    # Start the video stream
    stream_video(args.ip, args.port)
