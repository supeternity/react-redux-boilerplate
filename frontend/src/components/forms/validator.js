// this is an abstract class draw ?

// checks methods
const check = {
  email: function(val) {
    return !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(val)
  },
  required: function(req, values) {
    const res = {}
    for (let i = 0; i < req.length; i++) {
      if (!values[req[i]]) {
        res[req[i]] = 'Обязательно для ввода';
      }
    }
    return res;
  }
}

// public
export const VALIDATION_LOGIN = values => {
  const requiredFields = [
    "username",
    "password"
  ]
  const errors = Object.assign(
    {}, check.required(requiredFields, values)
  );
  if (values.username && check.email(values.username)) {
    errors.username = 'E-mail неправильный';
  }
  return errors;
}
