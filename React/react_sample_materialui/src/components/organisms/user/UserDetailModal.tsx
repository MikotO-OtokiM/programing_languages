import React, { memo, VFC } from 'react';
import { TextField } from '@material-ui/core';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';

import { User } from '../../../types/api/user';

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

type Props = {
  open: boolean;
  user: User;
  onClose: () => void;
  ariaLabelledby: string;
  ariaDescribedby: string;
}

export const UserDetailModal: VFC<Props> = memo((props) => {
  const { open, user, onClose, ariaLabelledby, ariaDescribedby } = props;
  const classes = useStyles();
  // getModalStyle is not a pure function, we roll the style only on the first render
  const [modalStyle] = React.useState(getModalStyle);

  const body = (
    <div style={modalStyle} className={classes.paper}>
      <form noValidate autoComplete="off">
        <TextField id="standard-basic" label="ユーザー名" value={user?.username} />
        <TextField id="filled-basic" label="氏名" value={user?.name} />
        <TextField id="outlined-basic" label="EMAIL" value={user?.email} />
        <TextField id="outlined-basic" label="TEL" value={user?.phone} />
      </form>
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
