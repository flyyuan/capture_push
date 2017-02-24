import os
ffmpeg_capture = 'ffmpeg -f dshow -i video="screen-capture-recorder" test.avi'
os.system(ffmpeg_capture)
