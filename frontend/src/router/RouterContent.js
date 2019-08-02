import React from "react";
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";

import Main from "../pages/Main";
import Links from "../pages/Links";
import CreateLink from "../pages/CreateLink";
import Project from "../pages/Project";
import Upload from "../pages/Upload";
import NotFound from "../components/NotFound";

function RouterContent({ route }) {
  switch (route.name) {
    case "main":
      return <Main />;
    case "links":
      return <Links />;
    case "create-link":
      return <CreateLink />;
    case "project":
      return <Project />;
    case "upload":
      return <Upload />;
    default:
      return <NotFound />;
  }
}

export default connect(routeNodeSelector(''))(RouterContent)
