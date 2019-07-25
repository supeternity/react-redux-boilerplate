import React from 'react';
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";

// material-ui components
import { Button } from '@material-ui/core';

// define styled-components
// &&* custom style priority
import styled from "styled-components";
const SpecialButton = styled(Button)`
  && {
    background: linear-gradient(45deg, #fe6b8b 30%, #ff8e53 90%);
    border-radius: 3px;
    border: 0;
    color: white;
    height: 48px;
    padding: 0 30px;
    box-shadow: 0 3px 5px 2px rgba(255, 105, 135, .3);
  }
`;

// compose
function goMaterialHelp() {
  window.open('https://material-ui.com/getting-started/usage', '_blank').focus()
}
function Main() {
  return (
    <>
      <h2>Keep<br/>calm<br/>and<br/>use</h2>
      <ul>
        <li>[ SASS or SCSS or CSS ] + <a href="https://facebook.github.io/create-react-app/docs/adding-a-css-modules-stylesheet" rel="noopener noreferrer" target="_blank">modules</a></li>
        <li>
          <SpecialButton onClick={goMaterialHelp}>
            Button custom
          </SpecialButton>
          <br/>
          <Button onClick={goMaterialHelp} variant="contained" color="primary">
            Contained button primary
          </Button>
          &nbsp;
          <Button onClick={goMaterialHelp} variant="contained" color="secondary">
            Contained button secondary
          </Button>
          <br/>
        </li>
      </ul>
    </>
  )
}

export default connect(routeNodeSelector(''))(Main)

// crazy reference for mapStateToProps and! mapDispatchToProps AND! this router
// https://github.com/nanopx/electron-react-redux-router5/blob/master/src/layouts/Counter.jsx