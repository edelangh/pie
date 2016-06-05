from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    file_path = '/tmp/pie.mp3'
    cmd_player = "mpg123 -q " + file_path
else:
    file_path = 'pie-tmp.mp3'
    cmd_player = 'C:/Program Files/VideoLAN/VLC/vlc.exe --intf dammy ' + file_path + ' vlc://quit'

lang = "en"
name = "pie"

hello = "Hello, I'm " + name + ". I'm created to serve you"
