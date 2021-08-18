// プライマリボタンのコンポーネント
import { Button } from "@material-ui/core";
import { memo, ReactNode, VFC } from "react";


type Props = {
  children: ReactNode;
  disabled?: boolean;
  loading?: boolean;
  onClick: () => void;
}

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const PrimaryButton: VFC<Props> = memo((props) => {
  const { children, disabled = false, loading = false, onClick } = props;
  return (
    // <Button
    //   bg="teal.400"
    //   color="white"
    //   _hover={{ opacity: 0.8 }}
    //   disabled={disabled || loading}
    //   isLoading={loading}
    //   onClick={onClick}
    // >
    //   {children}
    // </Button>
    <Button
      onClick={onClick}
    >
      {children}
    </Button>
  );
});