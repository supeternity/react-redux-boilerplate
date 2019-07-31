import React from "react";
import DialogTitle from '@material-ui/core/DialogTitle';
import Dialog from '@material-ui/core/Dialog';

export default function LoginDialogue(props) {
  const { onClose, open } = props;

  const handleClose = function() {
    onClose(false)
  }

  return (<>
    <Dialog onClose={handleClose} aria-labelledby="auth-dialog" open={open}>
      <DialogTitle id="auth-dialog">Авторизация</DialogTitle>
      Форма авторизации
    </Dialog>
  </>);
}
