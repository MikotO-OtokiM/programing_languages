//##############################################################################
// 関数（function 命令）
/**
 * 静的な構造を定義する
 * コードを解析するタイミングで関数を登録するため、関数定義が実行処理より後ろに
 * 記載されていても、実行可能
 */
console.log('getSquareArea 関数結果：' + getSquareArea(2, 3))
// 以下のように表示される
/**
 * getSquareArea 関数結果：6
 */

function getSquareArea(width, height) {
    return width * height;
}


//##############################################################################
// 関数（関数リテラル（無名関数））
/**
 * 1 回しか利用しないような関数を実行したい場合などで利用
 * function 命令と異なり、関数リテラル定義がその呼び出しより前に記載されている必要あり
 * ※アロー関数表記の利用を推奨
 */
const letGetSquareArea = function(width, height) {return width * height};
console.log('letGetSquareArea 関数リテラル結果：' + letGetSquareArea(3, 4))
// 以下のように表示される
/**
 * letGetSquareArea 関数リテラル結果：12
 */


//##############################################################################
// 関数（アロー関数）
/**
 * 関数リテラルをシンプルに記載したもの
 */
const arrowGetSquareArea = (width, height) => {return width * height};
console.log('arrowGetSquareArea アロー関数結果：' + arrowGetSquareArea(4, 5))
// 以下のように表示される
/**
 * arrowGetSquareArea アロー関数結果：20
 */

/**
 * 下記の条件に該当する場合は、さらにシンプルに表現することが
 * ・関数本体が 1 文しかない
 * 　→ ブロック {...} を省略可能。return を省略可能
 * ・引数が 1 個
 * 　→ 引数の () を省略可能
 * 　※引数がない場合、() は省略不可
 */

