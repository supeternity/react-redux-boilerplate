import React from "react";

const ContextMessage = function(props) {
  const { message,  } = props;
  if (message) {
    return (
      <>
        { message }
      </>
    );
  } else {
    return <></>
  }
  
};

export default ContextMessage;
