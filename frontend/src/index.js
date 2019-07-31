import React from "react";
import ReactDOM from "react-dom";
import "normalize.css";
import "./assets/scss/global.scss";
import "typeface-roboto";
import { Provider } from "react-redux";
import { RouterProvider } from "react-router5";
import configureRouter from "./router";
import configureStore from "./store";
import { ThemeProvider } from "styled-components";
import StylesProvider from "@material-ui/styles/ThemeProvider";
import { createMuiTheme } from "@material-ui/core/styles";
import App from "./App";

// global SCSS variables > js-object > ThemeProvider > all sub styled-components
import themeForStyledComponents from "./assets/scss/_variables.scss";

// material-ui config
import purple from '@material-ui/core/colors/purple';
import green from '@material-ui/core/colors/green';
const themeForMaterialUi = createMuiTheme({
  palette: {
    primary: green,
    secondary: purple,
  },
});

const router = configureRouter();
const store = configureStore(router);
const Compose = (
  <Provider store={store}>
    <RouterProvider router={router}>
      <ThemeProvider theme={themeForStyledComponents}>
        <StylesProvider theme={themeForMaterialUi}>
          <App />
        </StylesProvider>
      </ThemeProvider>
    </RouterProvider>
  </Provider>
);
router.start((err, state) => {
  ReactDOM.render(Compose, document.getElementById("root"));
});
