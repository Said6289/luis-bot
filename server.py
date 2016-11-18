
import requests
import lbot

INITIAL_ID = 263969345
ADDRESS='https://api.telegram.org/bot234875332:AAEtMhP4y8s4MhD68iCbznBTdRqYbo8rroI/'
MAX_UPDATES = 10

class Message:
    #minimum necessary parameters are text and chat_id
    def __init__ (self, text, chat_id):
        self.text = text
        self.chat_id = chat_id
        self.dict = {'text': self.text, 'chat_id': self.chat_id}
    
    #getter for the dictionary
    def toDict():
        return self.dict

    #add and extra key val pair
    def addKeyPair(key, val):
        self.dict[key] = val
    
#accepts the individual update, outputs the chat_id
def getChatId(msg):
    return msg['message']['chat']['id']


def getUpdates(last_id):
    offset = last_id + 1
    arguments = {'offset': offset,
                 'limit' : MAX_UPDATES
                
                }
    return sendReq('getUpdates', arguments).json()['result']

def getUpdateId(update):
    return update['update_id']

     

def sendReq(command, arguments):
    return requests.get(ADDRESS + command, params=arguments)


def run():
    #to initialize
    last_id = -100
    #forever
    while True:
        incomingMsgs = getUpdates(last_id)
        for update in incomingMsgs:
            print('got1')
            msg = Message(lbot.getLuisWord(), getChatId(update))
            sendReq('sendMessage', msg.dict)
            last_id = getUpdateId(update)
    


