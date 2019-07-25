import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";

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

export default connect(routeNodeSelector(''))(Content)

// crazy reference for mapStateToProps and! mapDispatchToProps AND! this router
// https://github.com/nanopx/electron-react-redux-router5/blob/master/src/layouts/Counter.jsx
