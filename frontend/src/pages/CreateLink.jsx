import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";
import NoUserAccess from "../components/NoUserAccess";

export class CreateLink extends React.Component {
  render() {
    const { account } = this.props;
    if (!account.usertoken) {
      return (<NoUserAccess />);
    } else {
      return (
        <>
          CreateLink.jsx <b>ACCESS</b>
        </>
      );
    }
  }
}

CreateLink = connect(routeNodeSelector('CreateLink'))(CreateLink);
const mapStateToProps = store => ({
  account: store.rootReducer.account
});
export default connect(mapStateToProps)(CreateLink);
