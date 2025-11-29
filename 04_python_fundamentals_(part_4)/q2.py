'''
Q2. Create a class Book with the following attributes:
• title
• author
• list of reviews
And add methods to:
• add a new review
• count reviews
• display all reviews
'''

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.reviews=[]
        self.total_reviews=0
        
    def add_review(self,review):
            self.reviews.append(review)
            self.total_reviews+=1
    
    def display_reviews(self):
        print(f"Reviews : {self.reviews}")
        
b = Book("Atomic Habits","James Clear")
b.add_review("OMG")
b.add_review("Awesome")
b.display_reviews()