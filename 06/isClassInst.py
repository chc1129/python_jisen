# クラス - インスタンスのひな型となるオブジェクト
# クラス変数- クラスオブジェクトが保持する変数

# クラス変数を持つクラスを定義
class Page:
	book_title = 'Python Practice Book'

Page.book_title # インスタンスがなくても参照できる
print( Page.book_title )


Page.book_title = 'No title' # クラス変数の更新
Page.book_title
print( Page.book_title )


# クラス変数にはインスタンスからもアクセス可能

first_page = Page()
second_page = Page()

# クラス変数にはインスタンスからも参照可能
first_page.book_title
print( first_page.book_title )


second_page.book_title
print( second_page.book_title )


# クラス変数を更新
Page.book_title = 'Python Practice Book'

# クラス変数はすべてのインスタンスで共有される
first_page.book_title
print( first_page.book_title )


second_page.book_title
print( second_page.book_title )


# これはインスタンス変数になる
first_page.book_title = '[Draft]Pytohn Practice Book'
first_page.book_title
print( first_page.book_title )


# クラス変数は変わっていない
second_page.book_title
print( second_page.book_title )


first_page.book_title # インスタンス変数
print( first_page.book_title )


# インスタンス変数を削除
del first_page.book_title

# インスタンスの属性にないため、クラスの属性が検索される
first_page.book_title
print( first_page.book_title )
