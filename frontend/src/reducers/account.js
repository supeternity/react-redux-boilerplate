export const initialState = {
  isAuth: false,
  fetching: false,
  error: null,
  user: {}
};

export function accountReducer(state = initialState, action) {
  switch (action.type) {
    case "GET_USER_LOAD":
      return {
        ...state,
        fetching: action.payload
      };
    case "GET_USER_ERROR":
      return {
        ...state,
        error: action.payload
      };
    case "GET_USER_SUCCESS":
      return {
        ...state,
        isAuth: true,
        user: action.payload
      };
    default:
      return state;
  }
}
