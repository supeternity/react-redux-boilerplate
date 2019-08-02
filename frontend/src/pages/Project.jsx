import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";
import NoUserAccess from "../components/NoUserAccess";

export class Project extends React.Component {
  render() {
    const { account } = this.props;
    if (!account.usertoken) {
      return (<NoUserAccess />);
    } else {
      return (
        <>
          Project.jsx <b>ACCESS</b>
        </>
      );
    }
  }
}

Project = connect(routeNodeSelector('Project'))(Project);
const mapStateToProps = store => ({
  account: store.rootReducer.account
});
export default connect(mapStateToProps)(Project);
