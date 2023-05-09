from core.marketplace.models import Product

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart =self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[str(product.id)] = {
                'product_id' : product.id,
                'name': product.name,
                'quantity': 1,
                'image': product.thumbnail.url,
                'price': int(product.price),
                'seller': str(product.user),
                'description': str(product.description)

            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    break
            self.save() # Agregar esta línea
        self.save()

    def save(self):
        self.session ["cart"] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.remove(product)
                break
        else:
            print("el producto no existe en el carrito")
        self.save()

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True