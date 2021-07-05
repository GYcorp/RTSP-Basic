import os
import cv2
import ffmpeg
import numpy as np

# you should have ffmpeg in your path
# https://github.com/kkroening/ffmpeg-python

# set ffmpeg path
bin_path = os.path.dirname(os.path.realpath(__file__))+"\\bin\\"
os.environ['PATH'] = os.environ['PATH'] + ';' + bin_path

STREAM_DEBUG = True

class StreamPipe():
    def __init__(self, url):
        self.url = url
        probe = ffmpeg.probe(self.url)

        for stream in probe['streams']:
            if stream["codec_type"] == 'video':
                self.is_video = True
                self.width = int(stream["width"])
                self.height = int(stream["height"])

        self.status = "stopped" # receiving, 


    def start(self):

        input = ffmpeg.input(self.url)
        video = input['v']
        # no delay https://stackoverflow.com/questions/16658873/how-to-minimize-the-delay-in-a-live-streaming-with-ffmpeg
        process_v = ffmpeg.output(video, 'pipe:', fflags='nobuffer', format='rawvideo', pix_fmt='bgr24') # bgr or rgb
        process_v = process_v.run_async(pipe_stdout=True)
        self.video_stream = process_v.stdout

        while True:
            if self.is_video:
                in_bytes_v = self.video_stream.read(self.width * self.height * 3)
                if not in_bytes_v:
                    print("no_bytes")
                in_frame = (
                    np
                    .frombuffer(in_bytes_v, np.uint8)
                    .reshape([self.height, self.width, 3])
                )
                #TODO call back here

                if STREAM_DEBUG:
                    cv2.imshow("in_frame", in_frame)
                    cv2.waitKey(1)


if __name__ == "__main__":
    # streampip = StreamPipe("simple/sample2.ts")
    streampip = StreamPipe("rtsp://127.0.0.1:8554/test")
    streampip.start()