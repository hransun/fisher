class BookViewModel:
    def __init__(self,book):
        self.title = book['title']
        self.publisher =book['publisher']
        self.pages = book['pages']
        self.price =book['price']
        self.summary =book['summary']
        self.image =book['image']
        self.author = book['author']
        self.isbn = book['isbn']
        self.pubdate =book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,[self.author, self.publisher, self.price])
        print(intros)
        return '/'.join(str(v) for v in intros)

class BookCollection:
    def __init__(self):
        self.total =0
        self.books =[]
        self.keyword =''

    def fill(self,yushu_book,keyworkd):
        self.total = yushu_book.total
        self.keyword = keyworkd
        self.books = [BookViewModel(book) for book in yushu_book.books ]






class _BookViewModel:
    @classmethod
    def package_single(cls,data,keyword):
        returned = {
            'books': [],
            'total':0,
            'keyword': keyword
        }

        if data:
            returned['total'] =1
            returned['books'] = [ cls.__cut_book_data(data)]


        return returned


    @classmethod
    def package_collection(cls,data,keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returned['total'] = (data['total'])
            returned['books'] = [cls.__cut_book_data(book) for book in data['books'] ]

        return returned



    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'pages': data['pages'] or '',
            'price': data['price'],
            'summary': data['summary'] or '',
            'image':data['image'],
            'author': ','.join(data['author'])
        }
        return book
