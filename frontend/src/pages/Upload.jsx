import React from "react";
import { connect } from "react-redux";
import { createRouteNodeSelector } from "redux-router5";

function Upload() {
  return (<>Upload.jsx</>);
}

export default connect(createRouteNodeSelector('project.upload'))(Upload)
// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
// crazy reference for mapStateToProps and! mapDispatchToProps AND! this router
// https://github.com/nanopx/electron-react-redux-router5/blob/master/src/layouts/Counter.jsx