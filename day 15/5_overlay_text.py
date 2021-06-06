from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from moviepy.audio.fx.all import volumex
from PIL import Image

source_path =os.path.join(SAMPLE_INPUTS,'sample.mp4')
source_audio_path =os.path.join(SAMPLE_INPUTS,'audio.mp3')

mix_audio_dir=os.path.join(SAMPLE_OUTPUTS,"mixed_audio")
os.makedirs(mix_audio_dir,exist_ok=True)
og_audio_path=os.path.join(mix_audio_dir,'og.mp3')
final_audio_path=os.path.join(mix_audio_dir,'overlay-audio.mp3')
final_video_path=os.path.join(mix_audio_dir,'overlay-video.mp4')

video_clip=VideoFileClip(source_path)

original_audio=video_clip.audio
original_audio.write_audiofile(og_audio_path)


background_audio_clip=AudioFileClip(source_audio_path)
# bg_music=background_audio_clip.subclip(0,video_clip.duration)
w,h=video_clip.size
fps=video_clip.fps

indro_duration=5
intro_text=TextClip("hello world!",fontsize=70,color='white',size=video_clip.size)
intro_text=intro_text.set_duration(intro_duration)
intro_text=intro_text.set_fps(fps)
intro_text=intro_text.set_pos("center")
intro_music=background_audio_clip.subclip(0,intro_duration)

intro_text=intro_text.set_audio(intro_music)
# intro_text.write_videofile(final_video_path)
watermark_text=TextClip("CFE",fontsize=30,color='white',align='East',size=(w,30))
watermark_text=watermark_text.set_fps(fps)
watermark_text=watermark_text.set_duration(video_clip.reader.duration)
watermark_text=watermark_text.set_position(("bottom"))


cvc=CompositeVideoClip([watermark_text,video_clip],size=video_clip.size)
cvc=cvc.set_duration(video_clip.reader.duration)
cvc=cvs.set_fps(fps)
cvc=cvc.set_audio(None)

final_clip=concatenate_videoclips([intro_text,cvc])
final_clip.write_videofile(final_video_path,codec='libx264',audio_codec="aac")