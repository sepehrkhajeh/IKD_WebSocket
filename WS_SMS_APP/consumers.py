from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ConnectionSMSWebSocket(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['code']
        self.group_name = f"G-{self.room_id}"
        
        # اضافه کردن به گروه
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name  
        )
        
        print("Connected to websocket")
        
        # پذیرش اتصال WebSocket
        await self.accept()
        
    async def disconnect(self, code):
        print("Disconnecting from server")
        print(f"Code: {code}")
        
        # حذف از گروه
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        
        
    async def receive_json(self, content):
        # این تابع به طور خودکار JSON دریافت می‌کند
        message = content['code']
        print(message)
        # ارسال پاسخ 'pong' به کلاینت
        await self.send_json({
                'clint': message
            })
        
        # ارسال پیام به گروه چت
        await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat_message',
                    'code': message
                }
            )
    
    async def chat_message(self, event):
        # دریافت پیام از گروه و ارسال آن به کلاینت
        message = event['code']
        
        # ارسال پیام به WebSocket کلاینت
        await self.send_json({
            'code': message
        })
