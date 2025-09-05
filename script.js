class Chatbot {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.typingIndicator = document.getElementById('typingIndicator');
        
        this.responses = {
            "xin chào": "Xin chào! Tôi có thể giúp gì cho bạn?",
            "chào": "Chào bạn! Rất vui được gặp bạn!",
            "hello": "Hello! How can I help you today?",
            "hi": "Hi there! What can I do for you?",
            "bạn là ai": "Tôi là chatbot AI được tạo ra để hỗ trợ bạn!",
            "cảm ơn": "Không có gì! Tôi luôn sẵn sàng giúp đỡ bạn!",
            "tạm biệt": "Tạm biệt! Hẹn gặp lại bạn lần sau!",
            "bye": "Goodbye! Have a great day!",
            "bạn có thể làm gì": "Tôi có thể trò chuyện với bạn, trả lời câu hỏi và hỗ trợ bạn!",
            "thời tiết": "Xin lỗi, tôi không thể kiểm tra thời tiết. Bạn có thể xem trên ứng dụng thời tiết!",
            "giúp": "Tôi có thể trò chuyện và trả lời các câu hỏi cơ bản. Hãy thử hỏi tôi điều gì đó!",
            "help": "I can chat and answer basic questions. Try asking me something!"
        };
        
        this.init();
    }
    
    init() {
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });
        
        this.messageInput.focus();
    }
    
    sendMessage() {
        const message = this.messageInput.value.trim();
        if (!message) return;
        
        this.addMessage(message, 'user');
        this.messageInput.value = '';
        
        this.showTypingIndicator();
        setTimeout(() => {
            this.hideTypingIndicator();
            const response = this.generateResponse(message);
            this.addMessage(response, 'bot');
        }, 1000 + Math.random() * 1000);
    }
    
    addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        const time = new Date().toLocaleTimeString('vi-VN', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
        
        messageDiv.innerHTML = `
            <div class="message-bubble">${this.escapeHtml(text)}</div>
            <div class="message-time">${time}</div>
        `;
        
        this.chatMessages.insertBefore(messageDiv, this.typingIndicator);
        this.scrollToBottom();
    }
    
    generateResponse(message) {
        const lowercaseMessage = message.toLowerCase();
        
        // Tìm kiếm phản hồi phù hợp
        for (const [key, value] of Object.entries(this.responses)) {
            if (lowercaseMessage.includes(key)) {
                return value;
            }
        }
        
        // Phản hồi mặc định
        const defaultResponses = [
            "Thú vị! Bạn có thể kể thêm về điều đó không?",
            "Tôi hiểu rồi. Còn điều gì khác bạn muốn nói?",
            "Điều đó nghe có vẻ thú vị! Bạn nghĩ sao về nó?",
            "Cảm ơn bạn đã chia sẻ! Tôi có thể giúp gì khác không?",
            "Hmm, tôi chưa hiểu rõ lắm. Bạn có thể giải thích thêm không?",
            "Đó là một ý kiến hay! Bạn còn suy nghĩ gì khác?",
            "Tôi đang học hỏi từ cuộc trò chuyện này. Còn gì nữa không?"
        ];
        
        return defaultResponses[Math.floor(Math.random() * defaultResponses.length)];
    }
    
    showTypingIndicator() {
        this.typingIndicator.style.display = 'flex';
        this.scrollToBottom();
    }
    
    hideTypingIndicator() {
        this.typingIndicator.style.display = 'none';
    }
    
    scrollToBottom() {
        setTimeout(() => {
            this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
        }, 100);
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Khởi tạo chatbot khi trang web được tải
document.addEventListener('DOMContentLoaded', () => {
    new Chatbot();
});
