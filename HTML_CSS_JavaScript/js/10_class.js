//##############################################################################
// クラス
/**
 * java などのように public や private などのアクセス修飾子はない
 * JavaScript では全てが public となる
 */
class Article {
    // コンストラクター
    constructor(title, url, intro) {
        this.title = title;
        this.url = url;
        this.intro = intro;
    }
    // ゲッター
    get title() {
        return this._title;
        /**
         * プロパティの先頭に _ を書くのは、プライベート変数として扱っていることを
         * 表すために慣例的に記載している
         * 実際にプライベート変数になるわけではない（外からアクセス可能）
         */
    }
    // セッター
    set title(value) {
        this._title = value;
    }
    // インスタンスメソッド
    toString() {
        return `${this.title}(${this.url})：${this.intro}`;
    }
    // 静的メソッド
    static className() {
        console.log('Article');
    }
}

// 静的メソッドの呼び出し（インスタンス作成なしで呼び出し可能）
Article.className();
// 以下のように表示される
/**
 * Article
 */

// インスタンスの作成とコンストラクターによるプロパティの初期化
const article = new Article(
    'タイトル',
    'http://sample.com',
    'サンプルクラスです'
);

// ゲッターによるプロパティの呼び出し
console.log(article.title);
// 以下のように表示される
/**
 * タイトル
 */

// インスタンスメソッドの呼び出し
console.log(article.toString());
// 以下のように表示される
/**
 * タイトル(http://sample.com)：サンプルクラスです
 */
