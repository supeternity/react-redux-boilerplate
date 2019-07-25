import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";

function Create() {
  return (<>Create.jsx</>);
}

export default connect(routeNodeSelector('links.create'))(Create)

// crazy reference for mapStateToProps and! mapDispatchToProps AND! this router
// https://github.com/nanopx/electron-react-redux-router5/blob/master/src/layouts/Counter.jsx