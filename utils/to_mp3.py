import os
from subprocess import Popen


def to_mp3(user_id):
    direct = f'media/{user_id}/videos'
    video_file = os.listdir(direct)[0]
    mp3_file = f"media/{user_id}/audios/{video_file.split('.')[0]}.mp3"
    if not os.path.exists(f'media/{user_id}/audios'):
        os.mkdir(f'media/{user_id}/audios')
    cmd = f'ffmpeg -i {direct}/{video_file} -codec:a libmp3lame -q:a 0 {mp3_file} -y'
    print(cmd)
    popen = Popen(cmd.split())
    popen.communicate()
