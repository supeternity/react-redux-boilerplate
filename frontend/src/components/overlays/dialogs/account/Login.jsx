import React from "react";
import { connect } from "react-redux";
import Dialog from "@material-ui/core/Dialog";
import { DialogTitle, DialogContent } from '@material-ui/core';
import LoginForm from "../../../forms/account/Login";

import { setLoginDialogue } from "../../../../actions/layout";
import { getUserToken } from "../../../../actions/account";

export class LoginDialog extends React.Component {
  render() {

    const {
      layout,
      setLoginDialogue,
      loginData,
      getUserToken,
      accout
    } = this.props;

    const handleClose = () => {
      setLoginDialogue(false);
    };

    const authorization = () => {
      getUserToken(loginData.values);
    }

    const nonFieldsErrors = accout.error ?
      accout.error.data.non_field_errors : [];

    return (
      <>
        <Dialog
          open={layout.login}
          onClose={handleClose}
          aria-labelledby="auth-dialog">
            <DialogTitle id="auth-dialog">Авторизация</DialogTitle>
            <DialogContent>
              <LoginForm onSubmit={authorization} errors={nonFieldsErrors} />
            </DialogContent>
        </Dialog>
      </>
    );

  }
}

const mapStateToProps = store => ({
  layout: store.rootReducer.layout,
  accout: store.rootReducer.account,
  loginData: store.form.LoginForm,
});
const mapDispatchToProps = dispatch => ({
  setLoginDialogue: value => dispatch(setLoginDialogue(value)),
  getUserToken: value => dispatch(getUserToken(value)),
});
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginDialog);
