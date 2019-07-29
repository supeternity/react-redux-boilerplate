import apiAction from "./core/apiAction";
import apiUrls from "../router/apiUrls";

import {
  USER_TOKEN_PROCESS,
  USER_TOKEN_SUCCESS,
  USER_TOKEN_FAILURE
} from "./accountTypes";

export function getUserToken(pair) {
  return apiAction({
    url: apiUrls.USER.LOGIN,
    onSuccess: setUserToken,
    onFailure: failUserToken,
    label: USER_TOKEN_PROCESS
  });
}

function setUserToken(data) {
  return {
    type: USER_TOKEN_SUCCESS,
    payload: data
  };
}

function failUserToken(error) {
  return {
    type: USER_TOKEN_FAILURE,
    payload: error
  };
}
