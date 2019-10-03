from twisted.internet.protocol import Protocol, ServerFactory
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
import random
import requests

URLS = [
    "http://actravel.ru/country_codes.html",
    "https://github.com/Kiril0l?tab=repositories",
    "https://openweathermap.org/current"
]

class Echo(Protocol):

    def __init__(self):
        super().__init__()
        data = requests.get(URLS[random.randint(0, 2)])
        lines = []
        for key, value in data.headers.items():
            lines.append(f"{key} {value}")
        header = "\r\n".join(lines + ["\r\n\r\n"])
        html = data.text
        self.response = f"{header}{html}".encode("utf-8")



    def dataReceived(self, data):
        self.transport.write(self.response)  #читаем и оправляем данные
        self.transport.loseConnection()  #закрываем соединение после обработки данных

class SrvFactory(ServerFactory):

    def  __init__(self, file_name):
        self.file = file_name

    # protocol= Echo    первый вариант
    def buildProtocol(self, addr):
        self.fd.write("{}\n".format(addr))  #записываем в лог файл
        return Echo()

    def startFactory(self):
        print("start")
        self.fd = open(self.file, "a")

    def stopFactory(self):
        print("stop")
        self.fd.close()

if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 5000)
    endpoint.listen(SrvFactory("server.log"))
    reactor.run()
    # factory = SrvFactory()           первый вариант
    # reactor.listenTCP(5000, factory)
    # reactor.run()
