import pytest
from classes.many_to_many import Article, Magazine, Author


class TestArticle:
    """Tests for the Article class in many_to_many.py"""

    def test_has_title(self):
        """Article is initialized with a title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        assert article_1.title == "How to wear a tutu with style"
        assert article_2.title == "Dating life in NYC"

    def test_title_is_immutable_str(self):
        """title is an immutable string"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")

        assert isinstance(article_1.title, str)

        # Ensure that title is immutable by expecting an AttributeError
        with pytest.raises(AttributeError):
            article_1.title = "New Title"

        # Ensure only valid types are allowed at initialization
        with pytest.raises(Exception):
            Article(author, magazine, 500)  # Titles should only be strings

    def test_title_is_valid(self):
        """title is between 5 and 50 characters inclusive"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")

        # Valid title
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        assert 5 <= len(article_1.title) <= 50

        # Short title (should raise an Exception)
        with pytest.raises(Exception):
            Article(author, magazine, "Test")  # Less than 5 characters

        # Long title (should raise an Exception)
        with pytest.raises(Exception):
            Article(author, magazine, "How to wear a tutu with style and walk confidently down the street")  # More than 50 characters

    def test_has_an_author(self):
        """Article has an author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_2, magazine, "Dating life in NYC")

        assert article_1.author == author_1
        assert article_2.author == author_2

    def test_author_of_type_author_and_mutable(self):
        """Author is of type Author and mutable"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")

        assert isinstance(article_1.author, Author)

        # Author should be mutable
        article_1.author = author_2
        assert isinstance(article_1.author, Author)
        assert article_1.author.name == "Nathaniel Hawthorne"

    def test_has_a_magazine(self):
        """Article has a magazine"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert article_1.magazine == magazine_1
        assert article_2.magazine == magazine_2

    def test_magazine_of_type_magazine_and_mutable(self):
        """Magazine is of type Magazine and mutable"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")

        assert isinstance(article_1.magazine, Magazine)

        # Magazine should be mutable
        article_1.magazine = magazine_2
        assert isinstance(article_1.magazine, Magazine)
        assert article_1.magazine.name == "AD"

    def test_get_all_articles(self):
        """Article class maintains a list of all articles"""
        Article.all = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert len(Article.all) == 2
        assert article_1 in Article.all
        assert article_2 in Article.all
