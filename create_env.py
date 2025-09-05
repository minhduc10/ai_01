# Script to create .env file automatically
import os

# API key from your existing code
api_key = "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"

# Kiểm tra xem file .env đã tồn tại chưa
if os.path.exists('.env'):
    print("✅ File .env đã tồn tại!")
    # Đọc và hiển thị nội dung
    with open('.env', 'r') as f:
        content = f.read()
        if 'OPENAI_API_KEYTST' in content:
            print("🔑 API key đã được cấu hình trong .env")
        else:
            print("⚠️ File .env tồn tại nhưng chưa có API key")
            # Thêm API key vào file
            with open('.env', 'a') as f:
                f.write(f'\nOPENAI_API_KEYTST={api_key}\n')
            print("✅ Đã thêm API key vào file .env")
else:
    # Tạo file .env mới
    try:
        with open('.env', 'w') as f:
            f.write(f'OPENAI_API_KEYTST={api_key}\n')
        print("✅ File .env đã được tạo thành công!")
        print(f"🔑 API key: {api_key[:20]}...")
    except Exception as e:
        print(f"❌ Không thể tạo file .env: {e}")
        print("💡 Hãy tạo file .env thủ công với nội dung:")
        print(f"OPENAI_API_KEYTST={api_key}")
