# bg_music.write_audofile()

final_audio=CompositeAudioClip([original_audio,bg_music])
final_audio.write_audiofile(final_audio_path,fps=original_audio.fps)



# new_audio=AudioFileClip(final_audio_path)
#final_clip =video_clip.set_audio(new_audio)

final_clip =video_clip.set_audio(final_audio)
final_clip.write_videofile(final_video_path,codec='libx264',audio_codec="aac")
