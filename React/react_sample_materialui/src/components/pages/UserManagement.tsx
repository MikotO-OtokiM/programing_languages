// ユーザー管理ページのコンポーネント
import { memo, VFC, useEffect, useCallback, useState } from "react";
import { Box, Grid, makeStyles } from "@material-ui/core";

import { UserCard } from "../organisms/user/UserCard";
import { useAllUsers } from "../../hooks/useAllUsers";
import { useSelectUser } from "../../hooks/useSelectUser";
import { UserDetailModal } from "../organisms/user/UserDetailModal";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  card: {
    padding: theme.spacing(2),
  },
}));

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const UserManagement: VFC = memo(() => {
  // ユーザー情報取得用
  const { getUsers, loading, users } = useAllUsers();
  // 選択したユーザー情報のモーダル表示用
  const { onSelectUser, selectedUser } = useSelectUser();

  // 初期処理
  // ユーザー情報を取得する
  // eslint-disable-next-line
  useEffect(() => getUsers(), []);

  // モーダル表示
  const [open, setOpen] = useState(false);
  const handleOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  // props として渡す関数は都度再作成するとレンダリングの効率が悪いためメモ化する
  const onClickUser = useCallback((id: number) => {
    onSelectUser({ id, users });
  }, [users, onSelectUser]);

  const classes = useStyles();

  return (
    <>
      <Grid container className={classes.root} spacing={2}>
        <Grid item>
          <Grid container className={classes.card} justifyContent="center" >
            {users.map((user) => (
              <Box key={user.id} onClick={handleOpen}>
                <UserCard
                  id={user.id}
                  userName={user.username}
                  fullName={user.name}
                  // 画像は unsplash からランダムに取得する
                  imageUrl="https://source.unsplash.com/random"
                  onClick={onClickUser}
                />
              </Box>
            ))}
          </Grid>
        </Grid>
      </Grid>
      <UserDetailModal
        open={open}
        user={selectedUser!}
        onClose={handleClose}
        ariaLabelledby="simple-modal-title"
        ariaDescribedby="simple-modal-description"
      />
    </>
  )
});