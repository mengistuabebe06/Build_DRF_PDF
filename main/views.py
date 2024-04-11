from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileUploadSerializer


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            # Process the uploaded file (e.g., save it, extract content, etc.)
            # You can access the uploaded file using serializer.validated_data['file']
            # Implement your logic here

            # Return a success response
            return Response(
                {"message": "File uploaded successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
