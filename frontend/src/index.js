import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { RouterProvider } from "react-router5";
import configureRouter from "./router";
import configureStore from "./store";
import "normalize.css";
import "./assets/scss/_global.scss";
import "typeface-roboto";
import Root from "./Root";
const router = configureRouter();
const store = configureStore(router);
const App = (
  <Provider store={store}>
    <RouterProvider router={router}>
      <Root />
    </RouterProvider>
  </Provider>
);
router.start((err, state) => {
  ReactDOM.render(App, document.getElementById("root"));
});
