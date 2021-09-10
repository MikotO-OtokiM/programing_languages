//##############################################################################
// 配列
const list = [
    'data0',
    'data1',
    ['data20','data21'],
];
// data0
console.log(list[0]);
// data21
console.log(list[2][1]);

// 配列の分割代入（アンパック）
const [l0, l1, l2] = list;
// data0
console.log(l0); 

// 末尾に要素の追加　★concat() での結合との違いに注意★
// push は配列の末尾に引数の要素を追加する　また戻り値は新しい配列の要素数となる
list.push('data3');
console.log(list);

// 末尾からの要素取得
console.log(list.pop());
console.log(list);

// スプレッド構文による展開
console.log(...list);
/**
 * 以下のように出力される
 * data0 data1 ["data20", "data21"]
 */

// スプレッド構文によるコピー
// ディープコピー（参照渡しではなく、新たな変数として作成される））
const list2 = [...list];
console.log(list2);

// map による各要素の加工
const list3 = list.map((data) => data + '_map');
console.log(list3);
/**
 * 以下のように出力される
 * ["data0_map", "data1_map", "data20,data21_map"]
 */

// filter による要素の取り出し（条件に該当するもののみ取得）
const numList = [1, 2, 3, 4, 5];
const numList2 = numList.filter((num) => num % 2 === 1);
console.log(numList2);
/**
 * 以下のように出力される
 * [1, 3, 5]
 */

// 配列の結合
// concat() 結合後の新しいオブジェクトを返す
console.log(numList.concat(numList2))
/**
 * 以下のように出力される
 * [1, 2, 3, 4, 5, 1, 3, 5]
 */


//##############################################################################
// 連想配列（辞書型） オブジェクトリテラル形式
/**
 * Map オブジェクト形式を利用することを推奨
 */
const dict = {
    a: 100,
    b: 200
};
// 100
console.log(dict.a);

// 連想配列の分割代入（アンパック）
const {a, b} = dict;
// 200
console.log(b);


//##############################################################################
// 連想配列（辞書型） Map オブジェクト形式
/**
 * オブジェクトリテラル形式との違い（メリット）
 * ・任意の型をキーにできる
 * ・空のマップを表現できる
 * ・サイズを取得できる（オブジェクトリテラル形式の場合は for...in で走査する必要あり
 * ・パフォーマンスに優れる
 */
const m = new Map([
    ['a_map', 100],
    ['b_map', 200],
])
// 100
console.log(m.get('a_map'));

// 要素の追加
m.set('c_map', 500);
console.log(m);


//##############################################################################
// 集合（セット）
const s = new Set(['ド', 'ミ', 'ソ']);
console.log(s);

// 要素の追加
s.add('レ');
console.log(s);


//##############################################################################
// シンボル
/**
 * 変数の名前そのものに意味を持たせて表現したい場合に利用
 * 文字列に似ているが違う
 * ・文字列/数値への暗黙的な型変換が行われない（エラーになる）
 * 列挙定数を表す場合などに利用し、if 文の条件判定時などでの曖昧さを排除する
 * 
 * const SUNDAY = Symbol('sunday');
 * ※引数はシンボルの説明。同じ引数のシンボルを作成しても、それらは別のシンボルとなる
 */
const SPRING = Symbol();
const SUMMER = Symbol();
const AUTUMN = Symbol();
const WINTER = Symbol();

let season = SPRING;
if (season === SPRING) {
    console.log('True');
}