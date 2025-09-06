from flask import jsonify
import os

def handler(request):
    api_key = os.getenv("OPENAI_API_KEYTST") or os.getenv("OPENAI_API_KEY")
    
    return jsonify({
        'status': 'ok',
        'message': 'Chatbot server is running!',
        'api_key_configured': bool(api_key),
        'environment': 'vercel'
    })

# For Vercel serverless functions
def main(request):
    return handler(request)
