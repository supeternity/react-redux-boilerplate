import { createStore, applyMiddleware, combineReducers, compose } from "redux";
import { router5Middleware, router5Reducer } from "redux-router5";
import { reducer as reduxFormReducer } from 'redux-form';
import { rootReducer } from "../reducers";
import apiMiddleware from "../core/middleware/api";
import thunk from "redux-thunk";
import logger from "redux-logger";

const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

export default function configureStore(router) {
  const store = createStore(
    combineReducers({
      router: router5Reducer,
      form: reduxFormReducer,
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
