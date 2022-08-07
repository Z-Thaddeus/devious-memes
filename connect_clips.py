import logging
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

logging.basicConfig(level=logging.INFO)
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

VIDEO_LOCATION = os.getenv('VIDEO_LOCATION')
EXPORT_LOCATION = os.getenv('EXPORT_LOCATION', 'youtube_video.mp4')

clips = []
dirs = os.listdir(os.path.join(__location__, VIDEO_LOCATION))
for index, file in enumerate(dirs):
    try:
        logging.info('Add Video to collection.')

        clips.append(VideoFileClip(os.path.join(VIDEO_LOCATION, file)))
    except OSError:
        pass

logging.info('Concatenate video clips.')
final_clip = concatenate_videoclips(clips, method='compose')
final_clip.write_videofile(EXPORT_LOCATION)
