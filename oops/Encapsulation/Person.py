class Person:
    def __init__(self,name,age,job):# __access
        self.name=name
        self.__age=age #means private data/variable
        self._job=job
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age