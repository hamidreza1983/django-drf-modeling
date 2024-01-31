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
    category = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset = Category.objects.all()
    )

   
    class Meta:
        model = Menu
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category, many=True).data

    
        return rep
          
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

class ChefsSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset = Skills.objects.all()
    )

    class Meta:
        model = Chefs
        fields = ['name','skills','status']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['skills'] = SkillsSerializer(instance.skills, many=True).data

        return rep
          
class ContactusSerializer(serializers.ModelSerializer):
    
     # def create(self, validated_data):
     #     validated_data['user'] = self.context.get('request').user
     #     return super().create(validated_data)    

     class Meta:
        model = Contactus
        fields = '__all__'                  