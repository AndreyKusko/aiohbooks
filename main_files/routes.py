from views import Authentication, base, books

routes = [
    ('GET',     '/',            base,           'base'),
    ('GET',     '/books/',      books,          'books'),
    ('*',       '/api/auth/',   Authentication, 'auth'),
]
