const SET_LOGIN_DIALOGUE = "SET_LOGIN_DIALOGUE";
export const setLoginDialogue = (bool) => {
  return dispatch => {
    dispatch({
      type: SET_LOGIN_DIALOGUE,
      payload: bool
    });
  };
};
