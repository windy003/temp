from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>YouTube 视频下载器</h1>
    <p>请输入 YouTube 视频链接：</p>
    <form method="post" action="/download">
        <input type="text" name="url" />
        <input type="submit" value="下载" />
    </form>
    """

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    video_id = url.split("v=")[1]
    video_info = get_video_info(video_id)

    if not video_info or "formats" not in video_info:
        return "无法获取视频信息", 400

    format_index = 0  # 简化处理：选择第一个格式

    video_file = download_video(video_id, format_index)

    if video_file and os.path.exists(video_file):
        return send_file(video_file, as_attachment=True)
    else:
        return "下载失败", 500

def get_video_info(video_id):
    # 使用 YouTube API 或 youtube-dl 获取视频信息
    # 这里是示例结构，需要根据实际情况进行修改
    video_info = {
        "formats": [
            {"resolution": "1080p", "format_id": "137"},
            {"resolution": "720p", "format_id": "136"},
            # 更多格式...
        ]
    }
    return video_info

def download_video(video_id, format_index):
    # 使用 youtube-dl 或类似工具下载视频
    # 这里应该返回视频文件的路径
    # 这是一个示例，需要根据您的下载逻辑进行修改
    file_path = "/path/to/your/downloaded/video.mp4"  # 替换为实际的文件路径
    # 实现下载逻辑
    # ...
    return file_path if os.path.exists(file_path) else None

if __name__ == "__main__":
    app.run(debug=True)
