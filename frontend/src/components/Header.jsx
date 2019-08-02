import React from "react";
import Nav from "./Nav";
import Account from "./Account";
import Grid from '@material-ui/core/Grid';

function Header() {
  return (
    <>
      <header>
        <Grid container>
          <Grid item xs={6}>
            <h1>Ceramic3D REACT SPA</h1>
          </Grid>
          <Grid item xs={6} align="right">
            <Account />
          </Grid>
        </Grid>
        <hr />
      </header>
      <Nav />
    </>
  );
}

export default Header;
