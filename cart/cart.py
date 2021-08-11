from store.models import Product
from decimal import Decimal
class Cart:

    # CREATE NEW SESSION
    def __init__(self, request):
        
        self.session = request.session
        # check if session is available
        cart= self.session.get('cartId')
        # build a session when new user visits the website
        if 'cartId' not in request.session:
        # if not available
            cart = self.session['cartId']={}
            #user to start with no session in the basket
        self.crt = cart

    def add(self, product, qty):
        '''  add product id to the session 
        '''
        product_id =  product.id

        if product_id not in self.crt:
            # product in not in the session data 
            self.crt[product_id]={'price':str(product.price), 'qty':(qty) }
            #add data(price) to the session based on the id
            self.session.modified = True
            # save
    # Add more data to the session data (images, )
    def __iter__(self):
        '''
        collect the product_id in the session data to quert database and return products
        '''
        product_ids = self.crt.keys()
        # get product ids from the session data
        products =Product.objects.filter(id__in = product_ids)
        #get id from product model
        cartt = self.crt.copy()
        # make a copy of session data

        for product in products:
            # merge session data and Product data to add more info to the session data
            cartt[str(product.id)]['producttt']  = product
            # cartt[str(product.id)] - matches product id that are in the basket
            # ['product']   - add more data from product
        for item in cartt.values():
            item['price'] = Decimal(item['price']) # convert price to decimal 
            item['total_price'] = item['price']* item['qty']
            yield item
    
    def  __len__(self):
        '''
        get basket data and count the quantity of items
        '''
        return sum(item['qty'] for item in self.crt.values())
        # capture single item(product) add quantity
        # use views.py to  capture and calculate multiple items products 

    # Total price
    def get_total_price(self):

        return sum(int(item['price']) * item['qty'] + int(400)  for item in self.crt.values()) 

    # Delete from session data
    def delete(self, product):
        product_id = str(product)
        # first convert product id to string as it wass added in the session in order to match

        if product_id in self.crt:
            del self.crt[product_id]
        self.session.modified= True

def save(self):
    self.session.modified= True
