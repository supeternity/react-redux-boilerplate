import {
  SET_LOGIN_DIALOGUE,
  SET_LOADER
} from "./layoutTypes";

export const setLoginDialogue = (bool) => {
  return dispatch => {
    dispatch({
      type: SET_LOGIN_DIALOGUE,
      payload: bool
    });
  };
};

export const setLoader = (bool) => {
  return dispatch => {
    dispatch({
      type: SET_LOADER,
      payload: bool
    });
  };
};
