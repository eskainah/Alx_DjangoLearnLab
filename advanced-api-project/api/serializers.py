from rest_framework import serializers
from .models import Book, Author

#a serializers for book model 
class BookSerializer(serializers.ModelSerializer)
    class Meta:
        model = Book
        field = '__all__'
    
    def validate(self, data):
        publication_year = data.get('publication_year')

        if publication_year > date.today().year:
            raise serializers.ValidationError(
                {'publication_year': 'Pulication date cannot be in the future!'}
            )
        return data
    
#a serializer for author model 
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class meta:
        model = Author
        fields = ['name', 'books']