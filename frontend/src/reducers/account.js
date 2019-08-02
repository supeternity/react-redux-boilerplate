import {
  USER_TOKEN_PROCESS,
  USER_TOKEN_SUCCESS,
  USER_TOKEN_FAILURE,
  USER_DATA_PROCESS,
  USER_DATA_SUCCESS,
  USER_DATA_FAILURE,
  USER_LOGOUT_PROCESS,
  USER_LOGOUT_SUCCESS,
  USER_LOGOUT_FAILURE,
} from "../actions/accountTypes";

export const initialState = {
  isAuth: false,
  error: null,
  currentUser: null
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
        isAuth: true,
        currentUser: action.payload
      };
    case USER_DATA_FAILURE:
      return {
        ...state,
        error: action.payload
      };
    case USER_LOGOUT_PROCESS:
      return {
        ...state,
        isAuth: false,
        usertoken: null,
        fetching: action.payload
      };
    case USER_LOGOUT_SUCCESS:
      return {
        ...state,
        isAuth: false,
        usertoken: null
      };
    case USER_LOGOUT_FAILURE:
      return {
        ...state,
        error: action.payload
      };
    default:
      return state;
  }
}
