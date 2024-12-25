from abc import ABC, abstractmethod

class NewsAgency(ABC):
    def __init__(self):
        self.observers = []
        self.news = ""

    def register_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for  observer in self.observers:
            observer.update(self.news)

    def set_news(self,news):
        self.news = news
        self.notify_observers()

class Subscriber(ABC):
    @abstractmethod
    def update(self,news):
        pass

class EmailSubscriber(Subscriber):
    def update(self,news):
        print(f"Email: {news}")

class SmsSubscriber(Subscriber):
    def update(self,news):
        print(f"SMS: {news}")

class WebSubscriber(Subscriber):
    def update(self,news):
        print(f"Web: {news}")

if __name__ == "__main__":
    newsagency = NewsAgency()

    emailsubscriber = EmailSubscriber()
    websubsciber = WebSubscriber()
    smssubscriber = SmsSubscriber()

    newsagency.register_observer(emailsubscriber)
    newsagency.register_observer(smssubscriber)
    newsagency.register_observer(websubsciber)

    newsagency.set_news("COVID-19 Emerged Again!")
    newsagency.remove_observer(smssubscriber)
    newsagency.set_news("COVID-19 Emerged Again!!!!!!")
