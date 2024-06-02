class Article:
    all = []

    def __init__(self, author, magazine, title):
        
        
        if not isinstance(title, str):
            raise ValueError("Tittle should be a string.")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance (magazine, Magazine):
            raise TypeError ("Magazine must be an instance of Magazine")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        
        Article.all.append(self)
        magazine._articles.append(self)
        author._articles.append(self)
    def __repr__(self):
        return f"Article(title={self.title}, author={self.author.name}, magazine={self.magazine.name})"
          
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")
    

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = value
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = value
        

        
        # @title.setter
        # def title(self, value):
        #     if hasattr(self, '_Article__title'):
        #         raise AttributeError("title is an immutable string")
        #     else:
        #         raise AttributeError("No title attribute found.")
        
class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 3 <= len(name) <= 50:
            raise ValueError("Name must be between 3 and 50 characters, inclusive")
        self._name = name
        self._articles = []
        Author.all.append(self)    

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, value):
            raise AttributeError("Name is immutable")

            

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))


    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles())) if self.articles() else None
    
    def __repr__(self):
        return f"Author(name={self.name})"



class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name    

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters long")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if not value:
            raise ValueError("Category cannot be empty")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] or None

    def contributing_authors(self):
        author_counts = {author: 0 for author in self.contributors()}
        for article in self._articles:
            author_counts[article.author] += 1
        return [author for author, count in author_counts.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        from collections import Counter
        magazine_counts = Counter(article.magazine for article in Article.all)
        if not magazine_counts:
            return None
        top_magazine, _ = magazine_counts.most_common(1)[0]
        return top_magazine

    def __repr__(self):
        return f"Magazine(name={self.name}, category={self.category})"