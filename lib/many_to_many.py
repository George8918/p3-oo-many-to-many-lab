class Author:
    members=[]

    def __init__(self,name):
      self.name = name
      self.members.append(self)

    def contracts(self):
        return[contract for contract in Contract.members if contract.author == self]
    
    def books(self):
        return[contract.book for  contract in self.contracts()]
    
    def sign_contract(self,book, date, royalties): 
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
class Book:
    members=[]

    def __init__(self,title):
        self.title= title
        self.members.append(self)
    
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
    
    def contracts(self):
        return [contract for contract in Contract.members if contract.book == self]

from datetime import datetime

class Contract:
    members=[]

    def __init__(self,author,book,date,royalties):

        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("Book must be of type Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author=author
        self.book=book
        self.date=date
        self.royalties=royalties
        self.members.append(self)

    
   
    @classmethod
      
    def contracts_by_date(cls, date=None):
        contracts = cls.members
        if date is not None:
            contracts = [contract for contract in cls.members if contract.date == date]
        return sorted(contracts, key=lambda c: (datetime.strptime(c.date, '%m/%d/%Y'), cls.members.index(c)))

