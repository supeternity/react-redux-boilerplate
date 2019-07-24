import React from "react";
import { connect } from "react-redux";
import { createRouteNodeSelector } from "redux-router5";

function Links() {
  return (<>Links.jsx</>);
}

export default connect(createRouteNodeSelector('links'))(Links)

// crazy reference for mapStateToProps and! mapDispatchToProps AND! this router
// https://github.com/nanopx/electron-react-redux-router5/blob/master/src/layouts/Counter.jsx