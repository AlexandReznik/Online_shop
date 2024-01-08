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


class BasketItemModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'


class CommentModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'text', 'created_date']