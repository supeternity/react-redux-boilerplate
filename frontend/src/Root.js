import React from "react";
import { connect } from "react-redux";

import Header from "./components/Header";
import Nav from "./components/Nav";
import Content from "./components/Content";

export function Root() {
  return (
    <>
      <Header/>
      <aside>
        <Nav/>
      </aside>
      <Content/>
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
