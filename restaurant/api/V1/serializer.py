from rest_framework import serializers
from ...models import Service ,Menu,Events,Order, Skills,Chefs,ContactUs






class ServiceSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Service
        fields =[
            "title" , "status", "content",
        ]
    
class MenuSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Menu
        fields =[
            "title" , "status", "content", "price", 
        ]
class EventsSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Events
        fields =[
            "title" , "content", "price", 
        ]       
   
