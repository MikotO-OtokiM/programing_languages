################################################################################
# クラス と クラス変数／クラスメソッド
"""
定義の際の引数
    Python3 以降では以下のように引数の object を記載しなくても実行できる
        class Person()
        class Person
    しかし、object を書く記載方法が暗黙のルールとなっていることが多い
    ※継承する際のベースクラスとして利用するという意味もあるため
self
    自分自身を指すオブジェクト
    クラス内で関数を定義する際には self を引数に含める必要あり
クラス変数
    作成されたオブジェクトで共有される変数
クラスメソッド
    クラスオブジェクトを作成しなくても クラス名.メソッド名 で実行できるメソッド
    メソッド定義時に @classmethod を記載し、引数に cls を渡す
"""
class Person(object):
    # クラス変数
    kind = 'human'

    # コンストラクタ
    # クラスのオブジェクトが作成されたときに実行される
    def __init__(self, name):
        self.name = name

    # クラスメソッド（cls を引数に定義）
    @classmethod
    def get_kind(cls):
        print(cls.kind)

    # 通常のメソッド（self を引数に定義）
    def say_something(self):
        print('I am {}.hello'.format(self.name))

    # デストラクタ
    # クラスのオブジェクトが削除される（利用されなくなる）ときに実行される
    def __del__(self):
        print('Bye')

# クラス変数、クラスメソッドはオブジェクト作成前にアクセス可能
print(Person.kind)
print(Person.get_kind())

# その他はオブジェクト作成後にアクセス可能
person = Person('Mike')
person.say_something()
print('###########')
# 以下のように表示される
"""
human
human
I am Mike.hello
###########
～
～（以降のプログラムの実行結果
～
Bye
"""


################################################################################
# クラスの継承、メソッドのオーバーライド
"""
継承したい親クラスを引数としてクラスを定義することで、その親クラスを継承できる
"""
# 親クラス（ベースクラスとなるため object を引数として定義）
class Car(object):
    # コンストラクタでモデルの名前をクラス変数として定義
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

# 子クラス（継承するだけ）
class NormalCar(Car):
    # 子クラスで独自の処理を記載しない場合は pass を書く
    pass

# 子クラス（メソッドのオーバーライド）
class Bus(Car):
    # メソッドのオーバーライド
    def run(self):
        print('bus run')

# 子クラス（super による親クラスのメソッド呼び出し）
class SportsCar(Car):
    # model のデフォルト値を指定するために親くらすのコンストラクタを実行
    def __init__(self, model='sports'):
        super().__init__(model)

# モデル名を指定してオブジェクトを作成
bus = Bus('Kankou')
print(bus.model)
# オーバーライドしたメソッドを実行
print(bus.run())

# モデル名を指定せずオブジェクトを作成（デフォルトのモデル名が使われる）
sprots = SportsCar()
print(sprots.model)

# 以下のように表示される
"""
Kankou
bus run
sports
"""

################################################################################
# プロパティーを使ったクラス属性の設定
"""
該当のクラス属性をクラス外から隠蔽したい場合、属性名の先頭に __ （アンダースコア2個）
を付けて定義する
※_（アンダースコア1個）にするとクラス外がらも更新できてしまう
外部からの呼び出し、更新用にゲッターとセッターを定義する
"""
class Animal(object):
    def __init__(self, type=None, enable_fly=False):
        self.type = type
        # __ を付けて属性を定義
        self.__enable_fly = enable_fly
        print('type:', type, 'enable_fly:', enable_fly)
    
    # ゲッターを定義（@property でデコレートする）
    @property
    def enable_fly(self):
        return self.__enable_fly

    # セッターを定義（@属性名.setter でデコレートする）
    @enable_fly.setter
    def enable_fly(self, is_enable):
        self.__enable_fly = is_enable

dog = Animal('dog')
# クラス外から該当属性を直接呼び出すとエラー（AttributeError）になる
# print(dog.__enable_fly)

# ゲッターを使うと参照可能
print(dog.enable_fly)

# セッターで更新可能（dog.enable_fly(True) と書かないことに注意）
dog.enable_fly = True
print(dog.enable_fly)

"""
以下のように記載すると、別の変数として値が再定義されてしまうため注意
dog.__enable_fly = '#########'
これは、クラス属性の __enable_fly を更新しているのではなく、
__enable_fly という名前の新しい属性として定義することを意味しているため
"""


################################################################################
# 抽象クラス
"""
抽象メソッドをもつクラス
Java等が抽象クラスに対応していたため、Pythonも途中から対応した
必要なければ使わないほうがよいという考え方もある
abc ライブラリをインポートし、メソッド定義時に @abstractmethod を記載することで
抽象メソッドであることを明示的に示す
"""
import abc
# 引数に mataclass=abc.ABCMeta を指定してクラスを定義
class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sing(self):
        # 継承した子クラス側で実装するため pass とする
        pass

class Adult(Person):
    # 抽象メソッドである sing を実装しないとエラーとなる
    # pass

    def sing(self):
        print('sing!')

    def run(self):
        print('Adult run')

adult = Adult()
adult.sing()


################################################################################
# 多重継承
"""
複数のクラスを継承すること
クラス定義時にカンマ区切りで複数クラスを指定することで可能
継承する複数のクラスに同じ名前のメソッドが存在する場合、先に書いたクラス側の
メソッドが実行されることに注意
抽象メソッドと同様に、必要なければ使わないほうがよいという考え方もある
abc ライブラリをインポートし、メソッド定義時に @abstractmethod を記載することで
抽象メソッドであることを明示的に示す
"""
class AdultCar(Adult, Car):
    pass

adultCar = AdultCar()
# run メソッドは Adult と Car の両方に存在するが、クラス定義時に Adult を先に
# 指定しているため、Adult の run メソッドが実行される
adultCar.run()
adultCar.sing()
# 以下のように表示される
"""
Adult run
sing!
"""


################################################################################
# 特殊メソッド
"""
__init__ のようにPythonで予め用意されているメソッド
よく使われるのは __str__
以下を参照
https://docs.python.org/ja/3/reference/datamodel.html#special-method-names
"""
class Book(object):
    def __init__(self, title):
        self.bookTitle = title
    
    def __str__(self):
        return 'title is' + self.bookTitle

book = Book('ABC')
# オブジェクト自体を print したときに __str__ で定義した文字列が表示される
print(book)
