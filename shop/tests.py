from django.test import TestCase
#from django_webtest import WebTest
from .models import Product , Category
# Create your tests here.
from django.test import Client
from django.core.validators import ValidationError


#เทสโมเดลประเภทสินค้า
class CategoryModelTest(TestCase):
  
    def setUp(self):
        self.c=Category(
                
                name="เสื้อยืด",
                slug="เสื้อ-ยืด",
                image="category/image.png",
        )
        self.c.save()

    def test_model_category_cancreate(self):
        self.assertEqual(self.c.id,1)
        self.assertEqual(self.c.name,"เสื้อยืด")
        self.assertEqual(self.c.slug,"เสื้อ-ยืด")
        self.assertEqual(self.c.image,"category/image.png")

    def test_model_category_canedit(self):
        self.c.name="เสื้อแขนยาว"
        self.c.save()
        self.c = Category.objects.get(pk=self.c.id)
        self.assertEqual(self.c.name,"เสื้อแขนยาว")


    def test_model_category_not_null(self):
        self.c.name=None
        self.c.slug=None
        self.c.image=None
        with self.assertRaisesMessage(ValidationError,"This field cannot be null."):
            self.c.full_clean()


class ProductModelTest(TestCase):

##test model product
    def setUp(self):
        
        self.p = Product(
                
                id=1,
                name="เสื้อยืดลายการ์ตูน",
                slug="เสื้อยืด-ลายการ์ตูน",
                description="เสื้อยืดใส่สบาย",
              
                price=100,
                image="product/image.png",
                available=True,
                created=True,
                updated=True,
                
        )
        self.p.save()
    
    def test_model_product_cancreate(self):
    
        self.assertEqual(self.p.id,1)
        self.assertEqual(self.p.name,"เสื้อยืดลายการ์ตูน")
        self.assertEqual(self.p.slug,"เสื้อยืด-ลายการ์ตูน")
        self.assertEqual(self.p.description,"เสื้อยืดใส่สบาย")
  
        self.assertEqual(self.p.price,100)
        self.assertEqual(self.p.image,"product/image.png")
        self.assertEqual(self.p.available,True)

'''
     
    def test_model_product_canedit(self):
        self.p.name="เสื้อแขนสั้นสไตล์วินเทจ"
        self.p.save()
        self.p = Product.objects.get(id=self.p.id)
        self.assertEqual(self.p.name,"เสื้อแขนสั้นสไตล์วินเทจ")
 

    def test_model_product_not_null(self):
        self.p.name=None
        self.p.slug=None
        
        self.p.description=None
        self.p.price=None
        self.p.image=None

        with self.assertRaisesMessage(ValidationError,"This field cannot be null."):
            self.p.full_clean()
   '''       
 ##  def test_model_product_not_null(self):


class ViewTest(TestCase):
    def test_homepage(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
      
        response = self.client.get("/0000/00/00/0-invalid/")
        self.assertEqual(response.status_code, 404)

#   def test_tab_menu(self):
