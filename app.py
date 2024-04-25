from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# 设置你的 OpenAI API 密钥
openai.api_key = 'z5PIV2z5l2eGVYk6xu2dT3BlbkFJgf63V5VUofhmQpzMgwCi'

@app.route('/')
def home():
    # 呈现一个简单的 HTML 页面或返回一个欢迎消息
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        # 从 POST 请求中获取 prompt
        data = request.get_json()
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        # 使用 OpenAI API 生成文本
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        
        # 从响应中提取生成的文本
        answer = response.choices[0].text.strip()
        return jsonify({'answer': answer})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
