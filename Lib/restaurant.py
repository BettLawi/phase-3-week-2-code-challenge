class Restaurant:
    def __init__(self,name):
        self._name = name
        self._reviews = [] # store reviews for this restaurant


    @property
    def name(self):
        return self._name

    #Object Relationship Methods
    def reviews(self):
        return self._reviews

    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)    



