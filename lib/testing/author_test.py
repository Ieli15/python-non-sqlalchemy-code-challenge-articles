import pytest
from classes.many_to_many import Article, Magazine, Author


class TestAuthor:
    """Tests for Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """Author name is of type str and cannot change"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)

        with pytest.raises(AttributeError, match="Author name is immutable and cannot be changed."):
            author_1.name = "ActuallyTopher"

        with pytest.raises(AttributeError, match="Author name is immutable and cannot be changed."):
            author_2.name = 2

    def test_name_len(self):
        """Author name is longer than 0 characters"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert hasattr(author_1, "name")
        assert len(author_1.name) > 0
        assert hasattr(author_2, "name")
        assert len(author_2.name) > 0

        with pytest.raises(ValueError, match="Name must be a non-empty string"):
            Author("")

    def test_topic_areas_are_unique(self):
        """Topic areas are unique"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Giorgio Faletti")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        author_1.add_article(magazine_1, "How to wear a tutu with style")
        author_1.add_article(magazine_1, "Dating life in NYC")
        author_1.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert len(set(author_1.topic_areas())) == len(author_1.topic_areas())
        assert len(author_1.topic_areas()) == 2
        assert "Fashion" in author_1.topic_areas()
        assert "Architecture" in author_1.topic_areas()
        assert author_2.topic_areas() is not None  # Ensure the method does not return None
        assert author_2.topic_areas() == []  # This now correctly returns an empty list
