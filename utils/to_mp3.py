from subprocess import Popen


def to_mp3(user_id, file):
    mp4_file = f'{file}'
    f = open(mp4_file, 'r')
    f.close()
    mp3_file = f'file_0.mp3'
    cmd = f'cmd ffmpeg -i {mp4_file} -vn -acodec copy {mp3_file} -y'
    print(cmd.split())
    popen = Popen(cmd.split())
    popen.terminate()
