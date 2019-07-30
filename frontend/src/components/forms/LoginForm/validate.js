export default function(values) {
    const errors = {};
    const requiredFields = [
      'username',
      'password'
    ];
    requiredFields.forEach(field => {
      if (!values[field]) {
        errors[field] = 'Обязательно для ввода';
      }
    });
    return errors;
  }
  