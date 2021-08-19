import React, { ChangeEvent, memo, useEffect, useState, VFC } from 'react';
import { TextField } from '@material-ui/core';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';

import { User } from '../../../types/api/user';
import { PrimaryButton } from '../../atoms/button/PrimaryButton';

function rand() {
  return Math.round(Math.random() * 20) - 10;
}

function getModalStyle() {
  const top = 50 + rand();
  const left = 50 + rand();

  return {
    top: `${top}%`,
    left: `${left}%`,
    transform: `translate(-${top}%, -${left}%)`,
  };
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    paper: {
      position: 'absolute',
      width: 400,
      backgroundColor: theme.palette.background.paper,
      border: '2px solid #000',
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
    },
  }),
);

const onClickUpdate = () => alert();

type Props = {
  open: boolean;
  user: User;
  isAdmin?: boolean;
  onClose: () => void;
  ariaLabelledby: string;
  ariaDescribedby: string;
}

export const UserDetailModal: VFC<Props> = memo((props) => {
  const { open, user, isAdmin = false, onClose, ariaLabelledby, ariaDescribedby } = props;

  //　State
  const [username, setUsername] = useState("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");

  // State のセット
  useEffect(() => {
    setUsername(user?.username ?? '')
    setName(user?.name ?? '')
    setEmail(user?.email ?? '')
    setPhone(user?.phone ?? '')
  }, [user])

  // イベント
  const onChangeUserName = (e: ChangeEvent<HTMLInputElement>) =>
    setUsername(e.target.value);
  const onChangeName = (e: ChangeEvent<HTMLInputElement>) =>
    setName(e.target.value);
  const onChangeEmail = (e: ChangeEvent<HTMLInputElement>) =>
    setEmail(e.target.value);
  const onChangePhone = (e: ChangeEvent<HTMLInputElement>) =>
    setPhone(e.target.value);


  const classes = useStyles();
  // getModalStyle is not a pure function, we roll the style only on the first render
  const [modalStyle] = React.useState(getModalStyle);

  const body = (
    <div style={modalStyle} className={classes.paper}>
      <form noValidate autoComplete="off">
        <TextField
          id="standard-basic"
          label="ユーザー名"
          value={username}
          onChange={onChangeUserName}
          disabled={!isAdmin}
        />
        <TextField
          id="filled-basic"
          label="氏名"
          value={name}
          onChange={onChangeName}
          disabled={!isAdmin}
        />
        <TextField
          id="outlined-basic"
          label="EMAIL"
          value={email}
          onChange={onChangeEmail}
          disabled={!isAdmin}
        />
        <TextField
          id="outlined-basic"
          label="TEL"
          value={phone}
          onChange={onChangePhone}
          disabled={!isAdmin}
        />
      </form>
      {/* 管理者の場合のみ更新ボタンを表示 */}
      {isAdmin && (
        <PrimaryButton onClick={onClickUpdate}>更新</PrimaryButton>

      )}
    </div>
  );

  return (
    <div>
      <Modal
        open={open}
        onClose={onClose}
        aria-labelledby={ariaLabelledby}
        aria-describedby={ariaDescribedby}
      >
        {body}
      </Modal>
    </div>
  );
});
