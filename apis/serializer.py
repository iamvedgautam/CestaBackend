from rest_framework import serializers
from apis import models


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Stock
        fields = '__all__'


class CestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cesta
        fields = '__all__'


class UserPortfolioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserPortfolio
        fields = '__all__'
