from rest_framework import serializers

from apps.news.models import New, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class NewsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = New
        fields = ['id', 'title', 'body', 'tags', 'main_image', 'created_at', 'updated_at', 'images']

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        new = New.objects.create(**validated_data)
        for image_data in images_data.getlist('images'):
            Image.objects.create(new=new, image=image_data)
        return new

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.main_image = validated_data.get('main_image', instance.main_image)
        instance.save()
        for image_data in images_data.getlist('images'):
            Image.objects.create(new=instance, image=image_data)
        return instance
