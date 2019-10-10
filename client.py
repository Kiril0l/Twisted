from twisted.internet.protocol import ClientFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
import event
from threading import Thread
import time


class Message():

    @event.Event.origin("new_message", post = True)
    def add_messafe(self, message):
        for _ in range(20):
            time.sleep(2)
        message.append("Text")


class ChatClient(LineReceiver):

    def __init__(self, name):
        self.name = name
        self.state = "OFFLINE"
        self.work = True
        event.Event(name = "new_message", callback=self.send_message)


    def connectionMade(self):
        pass

    def LineReceiver(self, line):
        if self.state == "ONLINE":
            print(line.decode("utf-8"))
        elif self.state == "OFFLINE":
            print(line.decode("utf-8"))
            self.sendLine("{}".format(self.name).encode("utf-8"))
            self.state = "ONLINE"

    def connectionLost(self, reason):
        print("Lost")

    def send_message(self, *args, **kwargs):
        try:
            message = MESSAGE[0]
        except IndexError:
            print("Error")
        else:
            del MESSAGE[0]
            self.sendLine("{}".format(message).encode("utf-8"))

class ChatClientFactory(ClientFactory):

    def __init__(self, name):
        self.name = name

    def clientConnectionFailed(self, connector, reason):
        print("Failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Close")
        reactor.stop()

    def buildProtocol(self, addr):   #создает соединение
        self.connection = ChatClient(self.name)
        message = Message()
        worker = Thread(target=message.add_message, args=(MESSAGE,))
        worker.start()
        return self.connection

    def send(self, message):
        self.connection.send_message(message)




if __name__ == "__main__":
    # import event
    #
    # def executor():
    #     print ("выполнелось событие")
    # class Test():
    #
    #
    #     @event.Event.origin("rest", post= True)
    #     def worker(self):
    #         print ("я генерирую союытие")
    #
    # ev = event.Event(name="rest")
    # ev.register("rest", executor) #то, что должно случится, если происходит событие
    #
    # test = Test()
    # test.worker()


    # # сделать парсер аргументов
    chat = ChatClientFactory("Kirill")
    reactor.connectTCP("192.168.4.123", 5000, chat)
    reactor.run()
