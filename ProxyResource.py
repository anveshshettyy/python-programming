from abc import ABC, abstractmethod

class ProtectedResource(ABC):
    @abstractmethod
    def access_resource(self):
        pass

class ProtectedResourceImp(ProtectedResource):
    def access_resource(self):
        print("Accessing Protected Resource...")

class ProxyResource(ProtectedResource):
    def __init__(self,resource):
        self.resource = resource
        self.access_count = 0

    def access_resource(self):
        if self.access_count < 5 :
            self.resource.access_resource()
            self.access_count += 1
        else:
            print("Maximum Limit Reached")

if __name__ == "__main__":
    resource = ProtectedResourceImp()
    proxy = ProxyResource(resource)

    for _ in range(6):
        proxy.access_resource()