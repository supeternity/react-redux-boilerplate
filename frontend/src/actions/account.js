const GET_USER_LOAD = "GET_USER_LOAD";
const GET_USER_SUCCESS = "GET_USER_SUCCESS";
const GET_USER_ERROR = "GET_USER_ERROR";

const mock = new Promise((resolve, reject) => {
  if (true) {
    resolve({
      name: 'Nino Katamadze',
      age: '28'
    })
  } else {
    reject({
      code: 404
    })
  }
});

export const getUser = () => {
  return dispatch => {
    dispatch({
      type: GET_USER_LOAD,
      payload: true
    })
    mock
      .then(resp => {
        dispatch({
          type: GET_USER_SUCCESS,
          payload: resp
        })
      })
      .catch(err => {
        dispatch({
          type: GET_USER_ERROR,
          payload: err
        })
      })
      .finally(() => {
        dispatch({
          type: GET_USER_LOAD,
          payload: false
        })
      })
  };
};
