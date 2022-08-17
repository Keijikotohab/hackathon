import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";


const Header = () => {
  return (
    <AppBar 
      sx={{ backgroundColor: "#26cad0" }}
      position="static"
      color="inherit"
    >
      <Toolbar
        variant="dense"
        sx={{
          margin: "0 auto",
          paddingTop: "10px",
          paddingLeft: "5px",
          paddingRight: "5px",
          width: "100%",
          maxWidth: "50%",
          display: "flex",
          justifyContent: "space-between",
        }}
        disableGutters
      >
        <Typography sx={{color:"#fff",fontSize:20,fontWeight:"bold",marginTop:-1}}>リマインドアプリ</Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
