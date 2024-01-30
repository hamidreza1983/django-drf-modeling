from rest_framework import serializers
from ...models import Service ,Menu,Events,Order, Skills,Chefs,ContactUs






class ServiceSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Service
        fields = '__all__'
    
class MenuSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Menu
        fields = '__all__'
          
    # def detail(self,obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.id)

    # def create(self, validated_data):
        
    #     validated_data['content'] = 'for this course'
    #     return super().create(validated_data)

class EventsSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Events
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     validated_data['user'] = self.context.get('request').user
    #     return super().create(validated_data)    

    class Meta:
        model = Order
        fields = '__all__'       


class SkillsSerializer(serializers.ModelSerializer):
    
     # def create(self, validated_data):
     #     validated_data['user'] = self.context.get('request').user
     #     return super().create(validated_data)    

     class Meta:
        model = Skills
        fields = '__all__'        

class ChefssSerializer(serializers.ModelSerializer):
    
     # def create(self, validated_data):
     #     validated_data['user'] = self.context.get('request').user
     #     return super().create(validated_data)    

     class Meta:
        model = Chefs
        fields = '__all__'      
class ContactusSerializer(serializers.ModelSerializer):
    
     # def create(self, validated_data):
     #     validated_data['user'] = self.context.get('request').user
     #     return super().create(validated_data)    

     class Meta:
        model = Contactus
        fields = '__all__'                  