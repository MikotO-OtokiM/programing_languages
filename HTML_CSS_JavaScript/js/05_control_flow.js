//##############################################################################
// if 文
let count = 10;
if (count < 0) {
    console.log('negative');
}
else if (count == 0) {
    console.log('zero');
}
else {
    console.log('positive');
}


//##############################################################################
// switch 文
/**
 * default 句は省略すべきではない
 * break がないと該当句以降の処理も実行されることに注意
 */
let bloodType = 'O';
switch(bloodType) {
    case 'A':
        console.log('A型です');
        break;
    case 'B':
        console.log('B型です');
        break;
    case 'O':
        console.log('O型です');
        break;
    case 'AB':
        console.log('AB型です');
        break;
    default:
        console.log('不明です');
        break;
}


//##############################################################################
// while 文と continue 文、break 文
let countValue = 0;
// 条件式が True の間繰り返す
while (countValue < 10) {
    if (countValue > 7) {
        console.log('break');
        // while 文を抜ける
        break;
    } else if (countValue === 2){
        countValue += 1
        console.log('continue');
        // 以降の処理は実施せず、繰り返し判定部分に戻る
        continue;
    }
    console.log(countValue);
    countValue += 1;
}
// 以下のように表示される
/**
 * 0
 * 1
 * continue
 * 3
 * 4
 * 5
 * 6
 * 7
 * break
 */


//##############################################################################
// for 文（for 命令）
/**
 * オブジェクト、配列などデータの型によらず利用できる形式
 * while 文と同様、break 文、continue 文を利用可能
 */
// 01_basic.js の list の要素を出力
for (let i = 0; i < 3; i++) {
    console.log(list[i]);
}
// 以下のように表示される
/**
 * data0
 * data1
 * ["data20", "data21"]
 */


//##############################################################################
// for 文（for...in 命令）
/**
 * オブジェクトのプロパティを順に列挙する形式
 * ※配列の場合は順序が保証されないため、利用しない方がよい
 */
// 01_basic.js の dict の要素を出力
for (let i in dict) {
    console.log(i + 'は、' + dict[i]);
}
// 以下のように表示される
/**
 * aは、100
 * bは、200
 */


//##############################################################################
// for 文（for...of 命令）
/**
 * 配列など列挙可能なデータの要素を順に列挙する形式
 */
// 01_basic.js の list の要素を出力
for (let i of list) {
    console.log(i);
}
// 以下のように表示される
/**
 * data0
 * data1
 * ["data20", "data21"]
 */


//##############################################################################
// 例外処理
try{
    // 存在しない変数の参照
    console.log(aaaaa);
} catch (ex) {
    // try 内の処理が失敗した場合のみ、実行される処理
    console.log('例外発生：' + ex.message);
    // 以下のように表示される
    /**
     * 例外発生：aaaaa is not defined
     */
} finally {
    // Exception が発生しても発生しなくても必ず実行される処理
    console.log('例外処理終了');
}
