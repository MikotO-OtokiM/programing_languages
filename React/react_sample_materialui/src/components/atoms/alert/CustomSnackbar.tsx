import React, { useEffect } from 'react';
import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert, { AlertProps } from '@material-ui/lab/Alert';
import { makeStyles, Theme } from '@material-ui/core/styles';

function Alert(props: AlertProps) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    width: '100%',
    '& > * + *': {
      marginTop: theme.spacing(2),
    },
  },
}));

type Props = {
  isOpen: boolean;
  autoHideDuration: number;
  severity: "error" | "warning" | "info" | "success";
  message: string;
}

export const CustomSnackbar = (props: Props) => {
  const { isOpen = false, autoHideDuration, severity, message } = props;

  const classes = useStyles();
  const [open, setOpen] = React.useState(false);

  // 初回レンダリング時のみ設定
  useEffect(() => setOpen(isOpen), []);

  const handleClose = (event?: React.SyntheticEvent, reason?: string) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
  };

  return (
    <div className={classes.root}>
      <Snackbar
        open={open}
        autoHideDuration={autoHideDuration}
        onClose={handleClose}
      >
        <Alert severity={severity}>
          {message}
        </Alert>
      </Snackbar>
    </div>
  );
}

