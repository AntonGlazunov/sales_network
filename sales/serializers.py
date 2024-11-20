from rest_framework import serializers

from sales.models import Factory, Product, Contacts, Retail, IE


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['email', 'country']


class FactorySerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = ['name', 'contact', 'product', 'date_create']


class RetailSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Retail
        fields = ['name', 'contact', 'product', 'supplier', 'debt', 'date_create']
        extra_kwargs = {'debt': {'read_only': True}}


class IESerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = IE
        fields = ['name', 'contact', 'product', 'supplier', 'debt', 'date_create']
        extra_kwargs = {'debt': {'read_only': True}}


