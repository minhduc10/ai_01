import json
import os
import openai

def handler(request):
    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # Handle OPTIONS request for CORS
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'status': 'ok'})
        }
    
    if request.method == 'POST':
        try:
            # Lấy API key từ environment variables
            api_key = os.getenv("OPENAI_API_KEYTST") or os.getenv("OPENAI_API_KEY")
            
            if not api_key:
                return {
                    'statusCode': 500,
                    'headers': headers,
                    'body': json.dumps({
                        'success': False,
                        'error': 'API key not configured',
                        'debug': 'No OPENAI_API_KEYTST or OPENAI_API_KEY found'
                    })
                }
            
            # Khởi tạo OpenAI client
            client = openai.OpenAI(api_key=api_key)
            
            # Parse request body
            if hasattr(request, 'get_json'):
                data = request.get_json()
            else:
                import json
                data = json.loads(request.data.decode('utf-8'))
            
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
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({
                    'success': True,
                    'message': reply
                })
            }
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({
                    'success': False,
                    'error': str(e)
                })
            }
    
    return {
        'statusCode': 405,
        'headers': headers,
        'body': json.dumps({'error': 'Method not allowed'})
    }
