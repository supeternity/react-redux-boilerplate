import React from 'react';
import { connect } from "react-redux";
import { routeNodeSelector } from "redux-router5";

import Button from '@material-ui/core/Button';

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
          <Button onClick={goMaterialHelp} variant="contained" color="secondary">
            & Go to Matrial-UI
          </Button>
        </li>
      </ul>
    </>
  )
}

export default connect(routeNodeSelector(''))(Main)

// crazy reference for mapStateToProps and! mapDispatchToProps AND! this router
// https://github.com/nanopx/electron-react-redux-router5/blob/master/src/layouts/Counter.jsx