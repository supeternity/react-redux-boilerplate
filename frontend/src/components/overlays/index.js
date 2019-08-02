import React from "react";

// dialogues
import Login from "./dialogs/account/Login";
// sidebars
// ... snackbars
import Loader from "./snackbars/Loader";
// themes etc...

const Overlays = () => {
  return (
    <>
      <Login />
      <Loader />
    </>
  );
}

export default Overlays;
