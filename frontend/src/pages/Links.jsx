import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";
import NoUserAccess from "../components/NoUserAccess";

export class Links extends React.Component {
  render() {
    const { account } = this.props;
    if (!account.usertoken) {
      return (<NoUserAccess />);
    } else {
      return (
        <>
          Links.jsx <b>ACCESS</b>
        </>
      );
    }
  }
}

Links = connect(routeNodeSelector('links'))(Links);
const mapStateToProps = store => ({
  account: store.rootReducer.account
});
export default connect(mapStateToProps)(Links);
