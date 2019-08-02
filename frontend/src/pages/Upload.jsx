import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";

function Upload() {
  return (<>Upload.jsx</>);
}

export default connect(routeNodeSelector('upload'))(Upload)