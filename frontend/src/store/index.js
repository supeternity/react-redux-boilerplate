import { createStore, applyMiddleware, compose } from "redux";
import { router5Middleware } from "redux-router5";
import { rootReducer } from "../reducers";
import thunk from "redux-thunk";
import logger from "redux-logger";

const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export default function configureStore(router) {
  return createStore(
    rootReducer,
    composeEnhancer(applyMiddleware(router5Middleware(router), thunk, logger))
  );
}
