from twilio.rest import Client 
account_sid = 'ACf27c2740fab9d6c70dcb279bc90c636f' 
auth_token = 'a4149cfbece9487c76678e945aa06dab' 
client = Client(account_sid, auth_token) 

def send_msg(): 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hey kindi tom',      
                              to='whatsapp:+916282801581' 
                          ) 
    print(message.sid)