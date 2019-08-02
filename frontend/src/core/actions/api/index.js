import { API } from "./types";

export default function apiAction({
    url = "",
    method = "",
    data = null,
    accessToken = null,
    onSuccess = () => {},
    onFailure = () => {},
    label = "",
    loader = null,
    headersOverride = null
  }) {
    return {
      type: API,
      payload: {
        url,
        method,
        data,
        accessToken,
        onSuccess,
        onFailure,
        label,
        loader,
        headersOverride
      }
    };
  }