import Header from "../component/header";
import React from "react";
import { Typography } from "@mui/material";
import Button from '@mui/material/Button';
import { HeaderBox, Padding, MainBox, AddButtonBox } from './style';

const Finish: React.FC = () => {
  const back =()=>{
      window.location.href = "/main"
    }
  return (
    <>
      <HeaderBox>
        <Header />
      </HeaderBox>
      <Padding />
      <MainBox>
        <AddButtonBox>
          <Typography sx={{fontSize:30,marginBottom:2}} >アップロード完了しました</Typography>
          <Button onClick={()=>back()} variant="outlined" color="inherit" component="label">
          アップロード画面に戻る
          </Button>
        </AddButtonBox>
      </MainBox>
    </>
  )
};


export default Finish;
