class Observer:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, entity):
        self.subscribers.append(entity)

    def unsubscribe(self, entity):
        self.subscribers.remove(entity)

    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.on_notify(event)
