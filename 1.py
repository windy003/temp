from flask import Flask, request, send_file
import youtube_dl
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
    video_file = download_video(video_id)

    if video_file:
        return send_file(video_file, as_attachment=True)
    else:
        return "下载失败", 500

def download_video(video_id):
    # 设置下载选项
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '/tmp/download/%(title)s.%(ext)s',  # 您需要更改这个路径
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            video_url = f"http://www.youtube.com/watch?v={video_id}"
            info = ydl.extract_info(video_url, download=True)
            video_title = info.get('title', 'downloaded_video')
            return os.path.join('/path/to/download', f"{video_title}.{info['ext']}")
        except Exception as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    app.run(debug=True)
