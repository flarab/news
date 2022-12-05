from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apps.news.models import New, Image


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Image
        fields = ['image']


class NewsSerializer(serializers.ModelSerializer):
    main_image = Base64ImageField()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = New
        fields = ['id', 'title', 'body', 'tags', 'main_image', 'created_at', 'updated_at', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        instance = super().create(validated_data)
        for image_data in images_data:
            Image.objects.create(new=instance, **image_data)
        return instance

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images')
        instance = super().update(instance, validated_data)
        for image_data in images_data:
            # Acá tendrás que decidir si quieres actualizar o crear
            #o bien, eliminar todas las imágenes y crearlas de nuevo
            #image = Image.objects.filter(new=instance)
            #image.delete()
            Image.objects.update_or_create(new=instance, **image_data)
        return instance