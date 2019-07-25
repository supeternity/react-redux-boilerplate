import React from "react";
import { connect } from "react-redux";

import Header from "./components/Header";
import Nav from "./components/Nav";
import RouterContent from "./router/RouterContent";

// material-ui components
// import Button from ...

// styled-components
import styled from "styled-components";
import adaptive from "./utils/createMediaQuery";
const RootContainer = styled.div`
  padding: ${p => p.theme.desctopRootContainerPadding};
  ${adaptive({
    device: "iPhone678",
    orientation: "",
    style: `
      padding: ${p => p.theme.mobileRootContainerPadding};
      background-color: red;
    `
  })}
  ${adaptive({
    device: "iPhoneX",
    orientation: "",
    style: `
      padding: ${p => p.theme.mobileRootContainerPadding};
      background-color: green;
    `
  })}
`;

// compose
export function Root() {
  return (
    <RootContainer>
      <Header />
      <Nav />
      <RouterContent />
    </RootContainer>
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
