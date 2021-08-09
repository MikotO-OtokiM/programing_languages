//##############################################################################
// == と　=== の違い
// 【注意】原則として == は利用しないこと
// 　　　　同様に、!= は利用せず、!== を利用すること
var i = 1       // 数値の 1
var j = "1"     // 文字列の "1"

if (i == j) {
    console.log('型が違っても True になる');
    // このような曖昧さを排除したい場合、シンボルを利用するとよい
}

if (i === j) {
    // 型が違うため False と判定される
} else {
    console.log('型が違うため False になる');
}


//##############################################################################
// ||（または） と　&&（かつ）の本当の意味
/**
 * || ： 左側が false の場合、右側を返す
 * && ： 左側が ture の場合、右側を返す
 */
const num1 = null;
const num2 = 100;

// 「未設定です」が出力
console.log(num1 || '未設定です');
// 「100」が出力
console.log(num2 || '未設定です');

// 「null」が出力
console.log(num1 && '何か設定されました');
// 「何か設定されました」が出力
console.log(num2 && '何か設定されました');