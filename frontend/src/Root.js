import React from "react";
import { connect } from "react-redux";

import Header from "./components/Header";
import Nav from "./components/Nav";
import RouterContent from "./router/RouterContent";

export function Root() {
  return (
    <>
      <Header/>
      <Nav/>
      <RouterContent/>
    </>
  );
}

const mapStateToProps = store => ({
  account: store.account
});
// const mapDispatchToProps = dispatch => ({
//   anyAction: value => dispatch(anyAction(value)),
// });

// export default connect(mapStateToProps, mapDispatchToProps)(Root);
export default connect(mapStateToProps)(Root);
