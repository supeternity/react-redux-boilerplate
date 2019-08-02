import React from "react";
import FormGroup from "@material-ui/core/FormGroup";
import { Field, reduxForm } from "redux-form";
import { renderFieldInput } from "../../../core/MUIReduxForms";
import NonFieldErrors from "../NonFieldErrors";
import { Button } from '@material-ui/core';

import { VALIDATION_LOGIN } from "../validator";
const validate = VALIDATION_LOGIN;

const LoginForm = props => {
  const { pristine, submitting, handleSubmit, errors } = props;
  return (
    <FormGroup>
      <form onSubmit={handleSubmit}>
        <div>
          <Field
            name="username"
            component={renderFieldInput}
            label="E-mail"
            autoFocus />
        </div>
        <div>
          <Field
            name="password"
            component={renderFieldInput}
            label="Пароль"
            type="password"
          />
        </div>
        <NonFieldErrors messages={errors} />
        <Button
          type="submit"
          disabled={pristine || submitting}
          variant="contained"
          color="primary">
          Войти
        </Button>
      </form>
    </FormGroup>
  );
};

export default reduxForm({
  form: "LoginForm",
  validate
})(LoginForm);
