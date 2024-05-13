from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):
    def test_create_product(self):
        """
        새로운 제품을 생성하고 응답을 검증합니다.
        """
        url = reverse('product_list')
        data = {'name': 'Test Product', 'price': 20, 'description' : 'good', "in_stock" :True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_get_product(self):
        """
        제품 목록을 가져오고 결과를 검증합니다.
        """
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):
    def test_delete_product(self):
        """
        특정 제품을 삭제하고 결과를 검증합니다.
        """
        # 먼저 테스트 제품을 생성합니다.
        product = Product.objects.create(name="Test Product", price=30)
        url = reverse('product_detail', args=[product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
        