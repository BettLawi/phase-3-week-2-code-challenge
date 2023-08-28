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

    # Aggregate and association methods    
    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, full_name):
        for customer in cls.customers:
            if customer.full_name == name:
                return customer
        return None        

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer.given_name for customer in cls.customers if customer.given_name == name]


