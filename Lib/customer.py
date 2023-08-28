from review import Review

class Customer:

    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name 

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
    
    # Object Relationship Methods
    def restaurant(self):
        reviewed_restaurants = set()
        for review in self.reviews:
            reviewed_restaurants.add(review.customer())
        return list(reviewed_restaurants)

    def add_review(self,restaurant,rating):
        self.reviews.append(Review(self, restaurant=restaurant, rating=rating))


