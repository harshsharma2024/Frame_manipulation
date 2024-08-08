import numpy as np
from moviepy.editor import *
from moviepy.video.fx.all import crop

def zigzag_position(t, amplitude1=100, frequency=2,amplitude2=100,most_left_col=-200,most_right_col=720,most_top_row=0,video_duration=15):
    # x = most_left_col + amplitude1 + amplitude1 * np.sin(2 * np.pi * frequency * t)
    x = most_left_col + (most_right_col - most_left_col) * (t / video_duration)
    y = most_top_row + amplitude2 + amplitude2 * np.sin(2 * np.pi * frequency * t)
    return (x, y) 

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

    image_width, image_height = image.size
    most_left_col = -image_width
    most_right_col = back.size[0]
    most_top_row = image_height
    most_bottom_row = back.size[1] - 2*image_height
    end_t = np.log(-most_left_col)/10 + first

    amplitude1 = (most_right_col - most_left_col) / 2
    amplitude2 = (most_bottom_row - most_top_row) / 2
    frequency = 0.3

    video_duration = back.duration

    print(video_duration)

    image = image.set_position(lambda t: zigzag_position(t,amplitude1,frequency,amplitude2,most_left_col,most_right_col,most_top_row,video_duration)).set_duration(video_duration)
    image = image.set_duration(video_duration)
    print(type(image), image.size)

    image.fps = 60
    finalList.append(image)



    print(type(finalList))
    videoTemp = CompositeVideoClip(finalList)
    videoTemp.write_videofile("zig-zag-movement" + ".mp4")

if __name__ == "__main__":
    func()