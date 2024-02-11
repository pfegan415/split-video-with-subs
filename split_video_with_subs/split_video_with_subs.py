import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip
import pysrt


def split_video(input_filepath: str, output_filepath: str, time_seconds: int):
    video = VideoFileClip(input_filepath)

    if time_seconds:
        video_part1 = video.subclip(0, time_seconds)
        video_part2 = video.subclip(time_seconds)
    else:
        video_part1 = video.subclip(0, float(video.duration/2))
        video_part2 = video.subclip(float(video.duration/2))

    video_part1.write_videofile(f"{output_filepath}_part_1.mp4", codec="libx264")
    video_part2.write_videofile(f"{output_filepath}_part_2.mp4", codec="libx264")


def split_subs(input_filepath: str, output_filepath: str, time_seconds: int):
    subs = pysrt.open(input_filepath)

    for sub in subs:
        if sub.end.hours*3600 + sub.end.minutes*60 + sub.end.seconds > time_seconds:
            subs_part_1 = subs[:sub.index]
            subs_part_2 = subs[sub.index:]
            break

    subs_part_2.shift(seconds=-time_seconds)

    srt_part1 = pysrt.SubRipFile(subs_part_1)
    srt_part2 = pysrt.SubRipFile(subs_part_2)

    srt_part1.save(f"{output_filepath}_part_1.srt")
    srt_part2.save(f"{output_filepath}_part_2.srt")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python app for splitting a video and associated subtitles into 2 sets')
    parser.add_argument('-sv','--source-video', help='Filepath to source video', required=True)
    parser.add_argument('-ss','--source-subtitles', help='Filepath to source subtitles', required=True)
    parser.add_argument('-st','--split-time', help='Time in second son which to split source video and subtitles', required=True)
    parser.add_argument('-o','--output-name', help='Filepath (excluding file extensions) of the output files', required=True)
    args = parser.parse_args()

    split_time = int(args.split_time)
    split_video(input_filepath=args.source_video, output_filepath=args.output_name, time_seconds=split_time)
    split_subs(input_filepath=args.source_subtitles, output_filepath=args.output_name, time_seconds=split_time)
