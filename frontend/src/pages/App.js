import React from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import routes from '../router';
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
// wrap <Route> and use this everywhere instead, then when
// sub routes are added to any route it'll work
function RouteWithSubRoutes(route) {
  return (
    <Route
      path={route.path}
      render={props => (
        // pass the sub-routes down to keep nesting
        <route.component {...props} routes={route.routes} />
      )}
    />
  );
}
function App() {
  return (
    <Router>
      <div className={styles.app}>
        <header>
          <h1>Ceramic3D React SPA Boilerplate</h1>
            { getWelcome() }
          <hr/>
        </header>
        <nav>
          <Link to="/manage">Список ссылок</Link>&nbsp;
          <Link to="/project">Страница проекта</Link>
        </nav>
        <content>
          {routes.map((route, i) => (
            <RouteWithSubRoutes key={i} {...route} />
          ))}
        </content>
      </div>
    </Router>
  );
}

export default App;
