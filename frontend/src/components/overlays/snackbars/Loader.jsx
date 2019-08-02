import React from "react";
import { connect } from "react-redux";
import Snackbar from '@material-ui/core/Snackbar';
import Fade from '@material-ui/core/Fade';


export class Loader extends React.Component {
  render() {

    const { layout } = this.props;

    return <>
      <Snackbar
        open={layout.XHRProgress ? true : false}
        TransitionComponent={Fade}
        ContentProps={{
          'aria-describedby': 'loader',
        }}
        message={
          <span id="loader">{
            layout.XHRProgress ? layout.XHRProgress : ''
          }</span>
        }
      />
    </>
  
  }
}

const mapStateToProps = store => ({
  layout: store.rootReducer.layout
});
export default connect(
  mapStateToProps
)(Loader);
