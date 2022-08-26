import Header from "../component/header";
import React from "react";
import { Typography } from "@mui/material";
import Button from '@mui/material/Button';
import { HeaderBox, Padding, MainBox, AddButtonBox, ImageBox } from './style';
import Yane from "../../images/yane.png"
import UploadImg from "../../images/upok.png"
import Topmodoru from "../../images/topmodoru.png"

const Finish: React.FC = () => {
  const back =()=>{
      window.location.href = "/home"
    }
  return (
    <>
      <ImageBox>
          <img style={{ width:"100%", marginRight: 0 }}  src={Yane} />
      </ImageBox>
      <Padding />
      <MainBox>
        <AddButtonBox>
          <ImageBox>
            <img style={{ width:500, marginRight: 0 }}  src={UploadImg} />
          </ImageBox>
          <Button sx={{marginTop:1}} onClick={()=>back()} color="inherit" component="label">
            <img style={{ width:180, marginRight: 0 }}  src={Topmodoru} />
          </Button>
        </AddButtonBox>
      </MainBox>
    </>
  )
};


export default Finish;
