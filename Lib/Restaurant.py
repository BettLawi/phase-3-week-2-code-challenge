class Restaurant:
    def __init__(self,name):
        self._name = name
        self._reviews = [] # store reviews for this restaurant


    @property
    def name(self):
        return self._name

