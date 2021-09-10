/**
 * MDN Web Docs
 * https://developer.mozilla.org/ja/docs/Web/JavaScript
 */

//##############################################################################
// 変数宣言（型指定は不要）
/**
 * ＜命名規則＞
 * 1. 1 文字目はアルファベット、アンダースコア、ドル記号のいずれか
 * 2. 2 文字目以降は 1 文字目で利用できる文字か、数字のいずれか
 * 3. 大文字、小文字は区別
 * 4. JavaScript の予約後は使えない
 *
 * 以前は var で宣言していたが、ES2015 より let（変数） と const（定数） が
 * 利用可能となった（const を優先して利用した方がよい）
 * var は主に以下の理由により利用しない方がよい
 * ・再宣言（同名の変数の定義）ができてしまうため
 * ・ブロックスコープが適用されないため
 * 【注意】
 *  html で複数のJSファイルを読み込む場合、let で宣言した変数は全てのファイル内で
 *  一意になる必要あり（別ファイルで再宣言されているとエラーになる）
 *
 *  ＜非推奨の変数宣言＞
 *  x;                    let を記載しない
 *  let x;                初期化していない
 *  let x = 1, y = 2;     1 行でまとめて宣言
 */

//##############################################################################
// 文字列の出力
/**
 * ＜console への出力＞
 * console.log('～～');
 * 
 * ＜ダイアログへの出力＞
 * window.alert('～～');
 * 
 * ＜html の指定の id の要素に出力＞
 * let　text1 = '01_basic.js'
 * document.getElementById('text1').textContent = text1;
 */

// 文字列はシングルクォート、ダブルクォートのどちらでもくくることができる
// シングルクォートを推奨
const text1 = 'Hello World! from 01_basic.js';
// console への出力
console.log(text1);
// ダイアログへの出力
window.alert(text1);
// html の指定の id の要素に出力
document.getElementById('text1').textContent = text1;

// バッククォートでくくると複数行の文字列を表現できる
// バッククォート内で変数を埋め込むことができる
const x = 'JavaScript';
const t = `複数行の文字列
を出力する${x}`;
console.log(t);

// 0 埋め
let zeroume = 1;
console.log(('000' + zeroume).slice( -3 ))
/**
 * 以下のように出力される
 * 001
 */