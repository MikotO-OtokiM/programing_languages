// HOMEページのコンポーネント
import { memo, VFC } from "react";
/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const Home: VFC = memo(() => {
  return <p>HOMEページです</p>
});