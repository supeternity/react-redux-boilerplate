import React from "react";

import Header from "./components/Header";
import Nav from "./components/Nav";
import RouterContent from "./router/RouterContent";

// material-ui components
// import Button from ...

// styled-components
import styled from "styled-components";
import adaptive from "./utils/createMediaQuery";
const AppContainer = styled.div`
  padding: ${p => p.theme.desctopAppContainerPadding};
  ${adaptive({
    device: "iPhone678",
    style: `
      padding: ${p => p.theme.mobileAppContainerPadding};
      background-color: red;
    `
  })}
  ${adaptive({
    device: "iPhoneX",
    orientation: "l",
    style: `
      padding: ${p => p.theme.mobileAppContainerPadding};
      background-color: green;
    `
  })}
`;

// compose
export function App() {
  return (
    <AppContainer>
      <Header />
      <Nav />
      <RouterContent />
    </AppContainer>
  );
}

export default App;
