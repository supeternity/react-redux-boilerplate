import { combineReducers } from "redux";

import { router5Reducer } from "redux-router5";
import { accountReducer } from "./account";
// import { managerReducer } from "./manager";
// import { designerReducer } from "./designer";

export const rootReducer = combineReducers({
  router: router5Reducer,
  account: accountReducer
  // manager: managerReducer,
  // designer: designerReducer
});
