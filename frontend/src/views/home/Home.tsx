import React from "react";
import Button from '@mui/material/Button';
import { Padding, ImageBox, ImageBoxBotton } from './style';
import Logo from "../../images/asset_1.png"
import Torii from "../../images/asset_2.png"
import Moji from "../../images/asset_3.png"


const Home: React.FC = () => {

  const toMain =()=>{
        window.location.href = "/main"
    }

  return (
    <>
      <Padding />
        <ImageBox>
          <img style={{ width:70, marginRight: 0 }}  src={Logo} />
        </ImageBox>
        <ImageBoxBotton onClick={()=>toMain()}>
          <img style={{ width:380, marginRight: 0, marginTop:10 }}  src={Torii} />
        </ImageBoxBotton>
        <ImageBox>
          <img style={{ width:280, marginTop: -356,marginLeft:-700 }}  src={Moji} />
        </ImageBox>
    </>

  )
};


export default Home;
