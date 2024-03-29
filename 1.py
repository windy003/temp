from flask import Flask, request, send_file, after_this_request
import yt_dlp
import os

app = Flask(__name__)

@app.route("/")
def index():
    # ... 之前的代码 ...

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    video_id = url.split("v=")[1]
    audio_file = download_audio(video_id)

    if audio_file and os.path.exists(audio_file):
        @after_this_request
        def remove_file(response):
            try:
                os.remove(audio_file)
            except Exception as error:
                app.logger.error("Error removing file: %s", error)
            return response

        return send_file(audio_file, as_attachment=True)
    else:
        return "下载失败", 500

# ... 其他函数 ...

if __name__ == "__main__":
    app.run(debug=True)
