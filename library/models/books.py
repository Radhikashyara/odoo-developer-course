from odoo import models, fields


class Author(models.Model):
    _name = 'author'
    _description = 'Author'

    name = fields.Char()
    address = fields.Text()


# book_id = fields.Many2one('books')

class BookCategory(models.Model):
    _name = 'books.category'
    _description = 'Book Category'

    name = fields.Char()


class BookDepartment(models.Model):
    _name = 'books.department'
    _description = 'Book Department'

    name = fields.Char()


class BookPublisher(models.Model):
    _name = 'books.publisher'
    _description = 'Book Publisher'

    name = fields.Char()


class Shelf(models.Model):
    _name = 'shelf'
    _description = 'Shelf'

    name = fields.Char()
    rack_id = fields.Many2one('rack')


class Rack(models.Model):
    _name = 'rack'
    _description = 'Rack'

    name = fields.Char()
    shelf_ids = fields.One2many('shelf', 'rack_id')


class LibraryDemo(models.Model):
    _name = 'books'
    _description = 'Library data'
    _sql_constraints = [('isbn_unique', 'unique(isbn)', 'Duplicate isbn not allowed')]

    name = fields.Char(string="Book Name", default="Book", required=True)
    book_description = fields.Text()
    price = fields.Float()
    # author_ids = fields.One2many('author', 'book_id')
    author_ids = fields.Many2many('author')
    isbn = fields.Integer()
    category_id = fields.Many2one('books.category')
    department_id = fields.Many2one('books.department')
    barcode = fields.Char()
    publisher_id = fields.Many2one('books.publisher')
    edition = fields.Char()  # Many 2 one
    date = fields.Date()
    shelf_id = fields.Many2one('shelf')



class BookIssue(models.Model):
    _name = 'book.issue'
    _description = 'Book issued'

    name = fields.Char(default="User", required=True)
    email = fields.Char()
    address = fields.Text()
    issue_date = fields.Date()
    return_date = fields.Date()
    dept_ids = fields.Many2one('books.department','department_id')
    cat_ids = fields.Many2one('books.category','category_id')
    image = fields.Image()
