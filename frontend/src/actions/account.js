import apiAction from "../core/actions/api";
import apiUrls from "../router/apiUrls";

import { setCookie } from "../core/utils/cookie";

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
} from "./accountTypes";


// usertoken
export function getUserToken(pair) {
  return apiAction({
    method: 'POST',
    url: apiUrls.USER.LOGIN,
    data: pair,
    onSuccess: setUserToken,
    onFailure: failUserToken,
    label: USER_TOKEN_PROCESS,
    loader: 'Авторизация...'
  });
}
function setUserToken(data) {
  setCookie('usertoken', data.usertoken)
  return {
    type: USER_TOKEN_SUCCESS,
    payload: data.usertoken
  };
}
function failUserToken(error) {
  return {
    type: USER_TOKEN_FAILURE,
    payload: error
  };
}

// current user
export function getCurrentUser(token) {
  return apiAction({
    method: 'GET',
    url: apiUrls.USER.CURRENT,
    accessToken: token,
    onSuccess: setCurrentUser,
    onFailure: failCurrentUser,
    label: USER_DATA_PROCESS,
    loader: 'Загрузка информации о пользователе'
  });
}
function setCurrentUser(data) {
  return {
    type: USER_DATA_SUCCESS,
    payload: data
  };
}
function failCurrentUser(error) {
  return {
    type: USER_DATA_FAILURE,
    payload: error
  };
}

// logout
export function logout() {
  return apiAction({
    method: 'POST',
    url: apiUrls.USER.CURRENT,
    onSuccess: successLogout,
    onFailure: failLogout,
    label: USER_LOGOUT_PROCESS,
    loader: 'Загрузка информации о пользователе'
  });
}
function successLogout(data) {
  return {
    type: USER_LOGOUT_SUCCESS,
    payload: data
  };
}
function failLogout(error) {
  return {
    type: USER_LOGOUT_FAILURE,
    payload: error
  };
}