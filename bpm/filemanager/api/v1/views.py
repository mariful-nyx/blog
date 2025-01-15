from rest_framework import viewsets, status
from rest_framework.response import Response
from bpm.filemanager.models import Image
from bpm.filemanager.api.v1.serializers import ImageSerializer
from bpm.utils import upload_image_to_supabase
from rest_framework.parsers import MultiPartParser, FormParser


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    parser_classes = (MultiPartParser, FormParser)  # Allow file upload parsing

    def create(self, request):

        image_file = request.FILES['image']
        
        try:
            # Upload the image to Supabase and get the URL
            file_url = upload_image_to_supabase(image_file)
            print(file_url)

            # Save the image metadata in the database
            # image = Image.objects.create(file_name=image_file.name, file_url=file_url)

            # Serialize the image metadata and return it in the response
            # serializer = ImageSerializer(image)
            return Response(status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)