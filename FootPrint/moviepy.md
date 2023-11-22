`pip install moviepy`

#### 视频处理工具

###### 视频截取

```python
from moviepy.editor import *
import time

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# 输入视频文件路径
input_video_path = "/Users/jiangsai/Desktop/demo.mp4"

# 设置开始时间和结束时间（格式：hh:mm:ss）
start_time_str = "00:00:46"
end_time_str = "00:01:23"

# 将时间字符串转换为秒数
start_time = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time_str.split(":")))
end_time = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time_str.split(":")))

# 截取指定时间段的片段
output_video_path = "/Users/jiangsai/Desktop/output.mp4"
ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname=output_video_path)




# 截取demo.mp4中的00:01:20 - 00:02:40
video = VideoFileClip('/Users/jiangsai/Desktop/demo.mp4')
video_sub = video.subclip(t_start=(00:01:20), t_end=(00:01:40))
# 将截取的视频写入新视频文件
new_file = str(int(time.time())) + '_subclip.mp4'
clip.write_videofile(new_file)
```





###### 视频转GIF

```python
from moviepy.editor import VideoFileClip
 
video_path = './video.mp4'
clip = VideoFileClip(video_path)
clip.write_gif('Dynamic_graph.gif')
#  clip.write_gif("Dynamic_graph.gif", fps=15)  #设置为每秒15帧，这将直接影响gif文件的大小
```

* GIF缩放

  ```python
  from moviepy.editor import *
   
  clip = (VideoFileClip("Video.mp4").subclip(1, 3).resize(0.1))  # 宽度和高度乘以 0.1
  clip.write_gif("Video.gif")
  ```

###### 

###### 

###### 

###### 