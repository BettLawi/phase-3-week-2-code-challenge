from customer import Customer
from restaurant import Restaurant

class Review: 
    all_reviews = []

    def __init__(self,customer,restaurant,rating):
        self._customer = customer
        self._restaurant = restaurant
        slef._rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self._rating    

    @classmethod
    def all(cls):
        return cls.all_reviews 

    # Object Relationship Methods    
    def customer(self):
        return self._customer

    def restaurant(self):
        self._restaurant    

 


