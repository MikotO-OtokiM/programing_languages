// HOMEページのコンポーネント
import { memo, VFC } from "react";

import { CustomSnackbar } from "../atoms/alert/CustomSnackbar";

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const Home: VFC = memo(() => {
  return (
    <>
      <p>HOMEページです</p>
      {/* 再レンダリング時にも表示されてしまう。ログイン時だけ表示できるようにしたい */}
      <CustomSnackbar
        isOpen={true}
        autoHideDuration={2000}
        severity="success"
        message="ログインしました"
      />
    </>
  );
});