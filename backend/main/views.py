import fitz  # PyMuPDF
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ExtractedData
from .serializers import ExtractedDataSerializer
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import fitz  # PyMuPDF
from io import BytesIO
from random import randint

nltk.download("punkt")


@api_view(["GET"])
def get_extracted_data(request):
    if request.method == "GET":
        extracted_data = ExtractedData.objects.all()
        serializer = ExtractedDataSerializer(extracted_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(
        {"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST
    )


@api_view(["POST"])
def process_pdf(request):
    if request.method == "POST" and request.FILES.get("pdf_file"):
        pdf_file = request.FILES["pdf_file"]

        # Extract nouns and verbs from PDF content
        pdf_content = extract_pdf_content(pdf_file)
        nouns, verbs = process_content(pdf_content)

        # Generate unique email address with random number
        email = generate_random_email()

        # Serialize the data
        data_to_save = {
            "pdf_file": pdf_file,
            "email": email,
            "nouns": nouns,
            "verbs": verbs,
        }
        serializer = ExtractedDataSerializer(data=data_to_save)

        if serializer.is_valid():
            try:
                # Check if email already exists
                existing_record = ExtractedData.objects.get(email=email)
                serializer.update(existing_record, data_to_save)
                return Response(
                    {"data": serializer.data, "message": "Data updated successfully"},
                    status=status.HTTP_200_OK,
                )
            except ExtractedData.DoesNotExist:
                # Save new record
                serializer.save()
                return Response(
                    {"data": serializer.data, "message": "Data saved successfully"},
                    status=status.HTTP_201_CREATED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "File not provided"}, status=status.HTTP_400_BAD_REQUEST)


def generate_random_email():
    # Generate a random number for email uniqueness
    random_number = randint(1000, 9999)
    return f"mengistuabebe{random_number}@gmail.com"


def extract_pdf_content(pdf_file):
    try:
        # Open the PDF file using PyMuPDF
        pdf_document = fitz.open(stream=BytesIO(pdf_file.read()))
        text = ""

        # Iterate through each page and extract text
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text += page.get_text()

        # Close the PDF document
        pdf_document.close()

        return text
    except Exception as e:
        # Log or handle the exception
        print(f"Error extracting PDF content: {e}")
        return ""


def process_content(content):
    tokens = word_tokenize(content)
    tagged = pos_tag(tokens)
    nouns = [word for word, pos in tagged if pos.startswith("NN")]
    verbs = [word for word, pos in tagged if pos.startswith("VB")]
    return " ".join(nouns), " ".join(verbs)
