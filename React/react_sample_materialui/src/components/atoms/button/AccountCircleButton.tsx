// アカウントボタンのコンポーネント
import { Button, IconButton, Menu, MenuItem } from "@material-ui/core";
import AccountCircle from '@material-ui/icons/AccountCircle';

import React, { memo, ReactNode, VFC } from "react";
import { useHistory } from "react-router-dom";


// type Props = {
//   children: ReactNode;
//   disabled?: boolean;
//   loading?: boolean;
//   onClick: () => void;
// }

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const AccountCircleButton: VFC = memo(() => {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);


  const handleMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const history = useHistory();
  const handleLogout = () => {
    history.push("/");
  };

  return (
    <>
              <IconButton
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleMenu}
                color="inherit"
              >
                <AccountCircle />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorEl}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={open}
                onClose={handleClose}
              >
                <MenuItem onClick={handleLogout}>ログアウト</MenuItem>
              </Menu>
            </>
  );
});