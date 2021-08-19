// プライマリボタンのコンポーネント
import { makeStyles } from "@material-ui/core";
import { Button } from "@material-ui/core";
import { memo, ReactNode, VFC } from "react";

const useStyles = makeStyles((theme) => ({
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

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
  const classes = useStyles();

  return (
    <Button
      // type="submit"
      fullWidth
      variant="contained"
      color="primary"
      className={classes.submit}
      disabled={disabled || loading}
      onClick={onClick}
    >
      {children}
    </Button>
  );
});