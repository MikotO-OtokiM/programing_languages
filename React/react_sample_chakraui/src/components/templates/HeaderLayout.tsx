// ヘッダー有りレイアウトのコンポーネント
import { memo, ReactNode, VFC } from "react";
import { Header } from "../organisms/layout/Header";

// props の型を定義
type Props = {
  children: ReactNode;
};

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const HeaderLayout: VFC<Props> = memo((props) => {
  // props を展開
  const { children } = props;
  return (
    <>
      {/* Header の下に渡されたコンポーネントの children を表示させる */}      
      <Header />
      {children}
    </>
  );
});