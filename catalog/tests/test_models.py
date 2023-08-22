from django.test import TestCase

# Create your tests here.

from catalog.models import Author, Genre, Language, Book, BookInstance


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Author.objects.create(first_name="Big", last_name="Bob")

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_birth").verbose_name
        self.assertEqual(field_label, "date of birth")

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field("date_of_death").verbose_name
        self.assertEqual(field_label, "died")

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f"{author.last_name}, {author.first_name}"

        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), "/catalog/author/1/")


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Genre.objects.create(name="Thriller")

    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field("name").max_length
        self.assertEqual(max_length, 200)

    def test_genre_model_name_field_help_text(self):
        genre = Genre.objects.get(id=1)
        help_text = genre._meta.get_field("name").help_text
        self.assertEqual(
            help_text, "Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
        )

    def test_object_name_is_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = f"{genre.name}"
        self.assertEqual(str(genre), expected_object_name)


class LanguageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Language.objects.create(name="English")

    def test_name_label(self):
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field("name").max_length
        self.assertEqual(max_length, 200)

    def test_genre_model_name_field_help_text(self):
        language = Language.objects.get(id=1)
        help_text = language._meta.get_field("name").help_text
        self.assertEqual(
            help_text,
            "Enter the book's natural language (e.g. English, French, Japanese etc.)",
        )

    def test_object_name_is_name(self):
        language = Language.objects.get(id=1)
        expected_object_name = f"{language.name}"
        self.assertEqual(str(language), expected_object_name)


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создание книги
        test_author = Author.objects.create(first_name="John", last_name="Smith")
        test_genre = Genre.objects.create(name="Fantasy")
        test_language = Language.objects.create(name="English")
        test_book = Book.objects.create(
            title="Book Title",
            summary="My book summary",
            isbn="ABCDEFG",
            author=test_author,
            language=test_language,
        )
        # Create genre as a post-step
        genre_objects_for_book = Genre.objects.all()
        test_book.genre.set(
            genre_objects_for_book
        )  # Присвоение типов many-to-many напрямую недопустимо
        test_book.save()

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")

    def test_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("genre").verbose_name
        self.assertEqual(field_label, "genre")

    def test_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("language").verbose_name
        self.assertEqual(field_label, "language")


class BookInstanceModelTest(TestCase):
    pass
