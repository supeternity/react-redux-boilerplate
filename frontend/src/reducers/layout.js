import {
  SET_LOGIN_DIALOGUE,
  SET_LOADER
} from "../actions/layoutTypes";


export const initialState = {
  // dialogues :: bool
  login: false,
  // snackbars :: null || string
  XHRProgress: null
};

export function layoutReducer(state = initialState, action) {
  switch (action.type) {
    case SET_LOGIN_DIALOGUE:
      return {
        ...state,
        login: action.payload
      };
    case SET_LOADER:
      return {
        ...state,
        XHRProgress: action.payload
      };
    default:
      return state;
  }
}
