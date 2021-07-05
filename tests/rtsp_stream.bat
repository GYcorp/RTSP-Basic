set video_path=%1
set PATH=%PATH%;%~dp0..\bin\
start rtsp-simple-server.exe
ffmpeg.exe -re -stream_loop -1 -i %video_path% -preset ultrafast -map 0:v -c:v:0 copy -f rtsp -rtsp_transport tcp rtsp://127.0.0.1:8554/test