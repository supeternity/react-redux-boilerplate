import React from "react";

import FormControl from "@material-ui/core/FormControl";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import Checkbox from "@material-ui/core/Checkbox";

export const renderFieldInput = ({
  input,
  label,
  meta: { touched, error },
  ...custom
}) => (
  <FormControl>
    <TextField label={label} {...input} {...custom} />
    <FormHelperText id="component-error-text">
      {touched && error}
    </FormHelperText>
  </FormControl>
);

export const renderCheckbox = ({ input, label }) => (
  <FormControlLabel
    control={
      <Checkbox
        checked={input.value ? true : false}
        onChange={input.onChange} />
    }
    label={label}
  />
);
