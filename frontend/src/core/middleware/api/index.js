// inspired by https://leanpub.com/redux-book
import axios from "axios";
import { API } from "../../actions/api/types";
import { accessDenied, apiError, apiStart, apiEnd } from "../../reducers/api";
import { setLoader } from "../../../actions/layout";
import getAccessToken from "../../utils/getAccessToken";

const apiMiddleware = ({ dispatch }) => next => action => {
  next(action);

  if (action.type !== API) return;


  console.log(action.payload)

  const {
    url,
    method,
    data,
    accessToken,
    onSuccess,
    onFailure,
    label,
    loader,
    headers
  } = action.payload;
  const dataOrParams = ["GET", "DELETE"].includes(method) ? "params" : "data";

  // axios default configs
  const HOST = process.env.REACT_APP_API_HOST;
  const PORT = process.env.REACT_APP_API_PORT;
  axios.defaults.baseURL = `http://${HOST}:${PORT}`;
  axios.defaults.headers.common["Content-Type"] = "application/json";
  axios.defaults.headers.common["Authorization"] = accessToken || getAccessToken();

  if (label) {
    dispatch(apiStart(label));
  }
  if (loader) {
    dispatch(setLoader(loader));
  }

  axios
    .request({
      url,
      method,
      headers,
      [dataOrParams]: data
    })
    .then(({ data }) => {
      dispatch(onSuccess(data));
    })
    .catch(error => {
      dispatch(apiError(error));
      dispatch(onFailure(error.response));

      if (error.response && error.response.status === 403) {
        dispatch(accessDenied(window.location.pathname));
      }
    })
    .finally(() => {
      if (label) {
        dispatch(apiEnd(label));
      }
      if (loader) {
        dispatch(setLoader(null));
      }
    });
};

export default apiMiddleware;
