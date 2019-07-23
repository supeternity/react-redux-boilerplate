import React from 'react';
import styles from './App.module.scss';
import Button from '@material-ui/core/Button';

function goMaterialHelp() {
  window.open('https://material-ui.com/getting-started/usage', '_blank').focus()
}

function getWelcome() {
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

function App() {
  return (
    <div className={styles.app}>
      <header>
        <h1>Ceramic3D React SPA Boilerplate</h1>
          { getWelcome() }
        <hr/>
      </header>
    </div>
  );
}

export default App;
