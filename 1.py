from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>YouTube 音频下载器</h1>
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
    audio_file = download_audio(video_id)

    if audio_file and os.path.exists(audio_file):
        return send_file(audio_file, as_attachment=True)
    else:
        return "下载失败", 500

def download_audio(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/path/to/download/%(title)s.%(ext)s',  # 修改为实际的下载路径
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            video_url = f"http://www.youtube.com/watch?v={video_id}"
            info = ydl.extract_info(video_url, download=True)
            audio_title = info.get('title', 'downloaded_audio')
            return os.path.join('/path/to/download', f"{audio_title}.mp3")
        except Exception as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    app.run(debug=True)
