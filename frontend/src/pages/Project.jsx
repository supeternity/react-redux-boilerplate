import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";
import NoUserAccess from "../components/NoUserAccess";
import { setLoginDialogue } from "../actions/layout";

export class Project extends React.Component {
  render() {
    const { account, setLoginDialogue } = this.props;
    if (!account.isAuth) {
      setLoginDialogue(true);
      return (<NoUserAccess />);
    } else {
      return (
        <>
          Project.jsx
        </>
      );
    }
  }
}

Project = connect(routeNodeSelector('Project'))(Project);
const mapStateToProps = store => ({
  account: store.rootReducer.account
});
const mapDispatchToProps = dispatch => ({
  setLoginDialogue: value => dispatch(setLoginDialogue(value))
});
export default connect(mapStateToProps, mapDispatchToProps)(Project);
