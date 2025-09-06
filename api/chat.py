from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import openai

# Nạp các biến môi trường từ file .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Cho phép CORS cho frontend

# Lấy API key từ biến môi trường (sử dụng file .env của bạn)
api_key = os.getenv("OPENAI_API_KEYTST") or os.getenv("OPENAI_API_KEY")

# Nếu không tìm thấy trong .env, in thông báo debug
if not api_key:
    print("🔍 Đang tìm kiếm API key...")
    print("📁 Đường dẫn hiện tại:", os.getcwd())
    print("📋 Các biến môi trường có sẵn:")
    for key in os.environ:
        if 'OPENAI' in key.upper():
            print(f"   - {key}: {os.environ[key][:20]}...")
    
    # Thử các tên biến khác có thể có
    api_key = (os.getenv("OPENAI_API_KEY") or 
               os.getenv("OPENAI_API_KEYTST") or 
               os.getenv("OPENAI_KEY"))
    
    if not api_key:
        print("❌ Không tìm thấy API key trong environment variables")
        api_key = "dummy-key"  # Fallback for deployment

client = openai.OpenAI(api_key=api_key) if api_key != "dummy-key" else None

def handler(request):
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
    
    if request.method == 'POST':
        try:
            if not client:
                return jsonify({
                    'success': False,
                    'error': 'API key not configured'
                }), 500
            
            # Lấy dữ liệu từ frontend
            data = request.get_json()
            messages = data.get('messages', [])
            
            print(f"📨 Received request with {len(messages)} messages")
            
            # Gọi OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=200
            )
            
            reply = response.choices[0].message.content
            print(f"✅ OpenAI response: {reply[:50]}...")
            
            return jsonify({
                'success': True,
                'message': reply
            })
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    return jsonify({'error': 'Method not allowed'}), 405

# For Vercel serverless functions
def main(request):
    return handler(request)
