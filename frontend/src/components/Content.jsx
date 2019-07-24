import React from "react";
import { connect } from "react-redux";
import { createRouteNodeSelector } from "redux-router5";

import Main from "../pages/Main";
import Links from "../pages/Links";
import Create from "../pages/Create";
import Project from "../pages/Project";
import Upload from "../pages/Upload";
import NotFound from "./NotFound";

function Content({ route }) {
  switch (route.name) {
    case "main":
      return <Main />;
    case "links":
      return <Links />;
    case "links.create":
      return <Create />;
    case "project":
      return <Project />;
    case "project.upload":
      return <Upload />;
    default:
      return <NotFound />;
  }
}

const mapStateToProps = state => createRouteNodeSelector('')(state.router);

export default connect(mapStateToProps)(Content);
