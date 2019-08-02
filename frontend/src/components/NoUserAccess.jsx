import React from "react";
import { connect } from "react-redux";
import { setLoginDialogue } from "../actions/layout";
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';

export class NoUserAccess extends React.Component {
  render() {
    const { setLoginDialogue } = this.props;
    const goToAuth = () => {
      setLoginDialogue(true);
    }
    goToAuth();
    return <Typography>
      Для доступа нужно <Link onClick={goToAuth}>авторизоваться</Link>
    </Typography>
  }
}

const mapStateToProps = store => ({
  account: store.rootReducer.account
});
const mapDispatchToProps = dispatch => ({
  setLoginDialogue: value => dispatch(setLoginDialogue(value))
});
export default connect(mapStateToProps, mapDispatchToProps)(NoUserAccess);
