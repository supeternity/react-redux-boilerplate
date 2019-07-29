import { createStore, applyMiddleware, combineReducers, compose } from "redux";
import { router5Middleware, router5Reducer } from "redux-router5";
import { rootReducer } from "../reducers";
import apiMiddleware from "../middleware/api";
import thunk from "redux-thunk";
import logger from "redux-logger";

const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export default function configureStore(router) {
  const store = createStore(
    combineReducers({
      router: router5Reducer,
      rootReducer
    }),
    composeEnhancer(applyMiddleware(
      router5Middleware(router),
      thunk,
      apiMiddleware,
      logger
    ))
  )
  window.store = store
  return store
}
