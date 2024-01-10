from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Product, Category, BasketItem, Comment


class ProductModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
