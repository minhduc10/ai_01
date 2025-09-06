import json
import os

def handler(request):
    api_key = os.getenv("OPENAI_API_KEYTST") or os.getenv("OPENAI_API_KEY")
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps({
            'status': 'ok',
            'message': 'Chatbot server is running!',
            'api_key_configured': bool(api_key),
            'environment': 'vercel',
            'api_key_preview': api_key[:15] + '...' if api_key else 'None'
        })
    }
