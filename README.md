# RTSP-Basic
rtsp 를 사용하는 기본 프레임 워크

# 테스트 방법
이 프로그램은 ffmpeg.exe 가 반드시 필요하다. 대부분의 명령어가 exe 의 pip 를 통해 진행되니 절대 ffmpeg.exe 를 먼저 설치할 것.
[google drive download](https://drive.google.com/file/d/1tH4KAX7DXKmwNY3Gv-uv9mF_xljJDeeU/view?usp=sharing)

1. rtsp 서버 실행

    tests/rtsp_stream.bat 을 실행하여 rtsp 서버를 시작한다.
    ```
    tests/rtsp_steam.bat [video path]
    ```

2. rtsp 동작 테스트

    tests/rtsp_play.bat 을 실행하여 rtsp 가 제대로 전송되고 있는지 확인한다.
    ```
    tests/rtsp_play.bat
    ```

3. python streaming 수신 코드 실행

    stream_receiver.py 를 통해 python 으로 스트리밍이 들어오는것을 확인한다.
    ```
    python steam_receiver.py
    ```