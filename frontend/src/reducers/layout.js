export const initialState = {
  // dialogues
  login: false
  // sidebars
  // ...
  // themes etc...
};

export function layoutReducer(state = initialState, action) {
  switch (action.type) {
    case "SET_LOGIN_DIALOGUE":
      return {
        ...state,
        login: action.payload
      };
    default:
      return state;
  }
}
