import React from "react";
import { connect } from "react-redux";

import { setLoginDialogue } from "../../actions/layout";
import LoginDialogue from "./LoginDialogue";

export class DialoguesOutput extends React.Component {
  render() {
    const { layout, setLoginDialogue } = this.props;
    return (
      <>
        <LoginDialogue open={layout.login} onClose={setLoginDialogue(false)} />
      </>
    );
  }
}

const mapStateToProps = store => ({
  layout: store.layout
});
const mapDispatchToProps = dispatch => ({
  setLoginDialogue: value => dispatch(setLoginDialogue(value))
});
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(DialoguesOutput);
