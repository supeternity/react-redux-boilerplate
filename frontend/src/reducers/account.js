import {
  USER_TOKEN_PROCESS,
  USER_TOKEN_SUCCESS,
  USER_TOKEN_FAILURE,
  USER_DATA_PROCESS,
  USER_DATA_SUCCESS,
  USER_DATA_FAILURE
} from "../actions/accountTypes";

export const initialState = {
  isAuth: false,
  error: null
};

export function accountReducer(state = initialState, action) {
  switch (action.type) {
    case USER_TOKEN_PROCESS:
      return {
        ...state,
        fetching: action.payload
      };
    case USER_TOKEN_SUCCESS:
      return {
        ...state,
        usertoken: action.payload
      };
    case USER_TOKEN_FAILURE:
      return {
        ...state,
        error: action.payload
      };
    case USER_DATA_PROCESS:
      return {
        ...state,
        fetching: action.payload
      };
    case USER_DATA_SUCCESS:
      return {
        ...state,
        currentUser: action.payload
      };
    case USER_DATA_FAILURE:
      return {
        ...state,
        error: action.payload
      };
    default:
      return state;
  }
}
