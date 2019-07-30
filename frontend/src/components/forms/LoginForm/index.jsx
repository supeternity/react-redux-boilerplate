import React from "react";
import validate from "./validate";

import FormGroup from "@material-ui/core/FormGroup";
import { Field, reduxForm } from "redux-form";
import { renderFieldInput, renderCheckbox } from "../../../core/MUIReduxForms";

const handleSubmit = function() {

  console.log('auth handle submit')
  
}

const LoginForm = props => {
  const { pristine, submitting } = props;
  return (
    <FormGroup>
      <form onSubmit={handleSubmit}>
        <div>
          <Field
            name="username"
            component={renderFieldInput}
            label="Логин"
          />
        </div>
        <div>
          <Field
            name="password"
            component={renderFieldInput}
            label="Пароль"
            type="password"
          />
        </div>
        <div>
          <Field
            name="remember_me"
            component={renderCheckbox}
            label="Запомнить на этом компьютере"
          />
        </div>
        <button type="submit" disabled={pristine || submitting}>
          Войти
        </button>
      </form>
    </FormGroup>
  );
};

export default reduxForm({
  form: "LoginForm", // a unique identifier for this form
  validate
})(LoginForm);
