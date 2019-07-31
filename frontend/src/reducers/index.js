import { combineReducers } from "redux";

import { accountReducer } from "./account";
import { layoutReducer } from "./layout";

export const rootReducer = combineReducers({
  account: accountReducer,
  layout: layoutReducer
});
