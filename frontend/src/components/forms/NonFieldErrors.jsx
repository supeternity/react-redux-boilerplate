import React from "react";
import ContextMessage from "../ContextMessage";

const NonFieldErrors = props => {
  const { messages } = props;
  const Stack = messages.map((msg, i) => 
    <ContextMessage
      message={msg}
      variant={"error"}
      key={`CM-${i}`} />
  );
  if (messages) {
    return <>{Stack}</>;
  } else {
    return <></>
  }
  
}

export default NonFieldErrors;
