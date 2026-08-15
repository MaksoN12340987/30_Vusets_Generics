from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # email = serializers.EmailField()
    # username = serializers.CharField(max_length=100)

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "is_active", "groups"]
