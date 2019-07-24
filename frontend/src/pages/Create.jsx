import React from "react";
import { connect } from "react-redux";
import { createRouteNodeSelector } from "redux-router5";

function Create() {
  return (<>Create.jsx</>);
}

export default connect(createRouteNodeSelector('links.create'))(Create)

// crazy reference for mapStateToProps and! mapDispatchToProps AND! this router
// https://github.com/nanopx/electron-react-redux-router5/blob/master/src/layouts/Counter.jsx