#delete audio of video
import moviepy.editor as mp

output_movie = '11 Python Tutorial for Beginners  Operators in Python.mp4'

final_clip=mp.VideoFileClip('11 Python Tutorial for Beginners  Operators in Python.mp4')

final_clip.write_videofile(output_movie, remove_temp=False, bitrate="5000k",audio=False,audio_codec="aac",codec='mpeg4')
print('hii')

