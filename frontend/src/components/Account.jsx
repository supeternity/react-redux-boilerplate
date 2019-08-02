import React from "react";
import { connect } from "react-redux";
import { setLoginDialogue } from "../actions/layout";
import { getCurrentUser, logout } from "../actions/account";
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';

export class Account extends React.Component {
  render() {
    const {
      account,
      setLoginDialogue,
      getCurrentUser,
      logout
    } = this.props;
    const goToAuth = () => {
      setLoginDialogue(true);
    }
    const userLogout = () => {
      logout();
    }
    if (!account.isAuth) {
      if (account.usertoken) {
        getCurrentUser(account.usertoken)
        return <>
            <p>Вход...</p>
        </>
      } else {
        return <>
          <Typography>
            <Link onClick={goToAuth}>Вход</Link>
          </Typography>
        </>
      }        
    } else {
      setLoginDialogue(false);
      return <>
          <Typography>
            <Link onClick={userLogout}>Выход</Link>
          </Typography>
        </>
    }
  }
}

const mapStateToProps = store => ({
  account: store.rootReducer.account
});
const mapDispatchToProps = dispatch => ({
  setLoginDialogue: value => dispatch(setLoginDialogue(value)),
  getCurrentUser: value => dispatch(getCurrentUser(value)),
  logout: value => dispatch(logout(value))
});
export default connect(mapStateToProps, mapDispatchToProps)(Account);
