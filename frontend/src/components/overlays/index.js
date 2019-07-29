import React from "react";
import { connect } from "react-redux";

// dialogues
import { setLoginDialogue } from "../../actions/layout";
import LoginDialogue from "./LoginDialogue";
// sidebars
// ...
// themes etc...

export class Overlays extends React.Component {
  render() {
    const { layout, setLoginDialogue } = this.props;
    return (
      <>
        <LoginDialogue open={layout.login} onClose={setLoginDialogue} />
      </>
    );
  }
}

const mapStateToProps = store => ({
  layout: store.rootReducer.layout
});
const mapDispatchToProps = dispatch => ({
  setLoginDialogue: value => dispatch(setLoginDialogue(value))
});
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Overlays);
