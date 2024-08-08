import numpy as np
from moviepy.editor import *
from moviepy.video.fx.all import crop

def func():
    finalList = []
    first = 4

    cum = 15

    backTemp = VideoFileClip("../Assets/video.mp4")

    if backTemp.duration >= cum:
        backTemp = backTemp.subclip(0, cum)
    elif backTemp.duration < cum:
        backTemp = backTemp.loop(duration = cum)


    (w, h) = backTemp.size

    if (w == 1200) & (h == 1800):
        back = backTemp
    else:
        backCropped = crop(backTemp, width= h/(w/h), height=h, x_center=w/2, y_center=h/2)
        back = backCropped.resize((1200,1800))


    finalList.append(back)

    image = ImageClip('../Assets/image.png', duration=cum)

    image = image.resize((200, 200))


    most_left_col = -image.size[0]
    most_right_col = back.size[0] 
    end_t = np.log(-most_left_col)/10 + first

    video_duration = back.duration

    print(video_duration)

    image = image.set_position(lambda t: (most_left_col + (most_right_col - most_left_col) * (t / video_duration), 200))
    image = image.set_duration(video_duration)
    print(type(image), image.size)

    image.fps = 60
    finalList.append(image)



    print(type(finalList))
    videoTemp = CompositeVideoClip(finalList)
    videoTemp.write_videofile("left_to_write_movement" + ".mp4")


if __name__ == "__main__":
    func()