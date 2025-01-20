from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from bpm.filemanager.models import Image
from bpm.filemanager.api.v1.serializers import ImageSerializer, ImageCreateSerializer
from supabase import create_client, Client
from django.conf import settings

supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


class ImageUploadView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ImageCreateSerializer
        else:
            return ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            file_name = image.name
            file_data = image.read()

            # Upload image to Supabase storage (which is AWS S3-like)
            try:
                response = supabase.storage.from_('avatars').upload(file_name, file_data)

                if response:
                    # Extract the public URL from the response data
                    public_url = supabase.storage.from_('avatars').get_public_url(file_name)
                    
                    image = Image.objects.create(
                        image = public_url,
                        image_alt_text = file_name
                    )
                    image.save()

                    return Response({"message": "Image uploaded successfully", "id": image.id, "url": public_url}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Upload failed", "details": response.get('error')}, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

