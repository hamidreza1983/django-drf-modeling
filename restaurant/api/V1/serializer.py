from rest_framework import serializers
from ...models import *

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['skills'] = ServiceSerializer(instance.skills).data
        return rep
    
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep

   
class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'
       
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'