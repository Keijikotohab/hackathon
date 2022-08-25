import { styled } from '@mui/material/styles';

export const HeaderBox = styled("div")(() => ({
  zIndex: 19, 
  position: "fixed", 
  width: "100%"   
}));

export const Padding = styled("div")(() => ({
  height: 80
}));

export const MainBox = styled("div")(() => ({
  width: "50%",
  marginLeft: "auto",
  marginRight: "auto",
  marginTop: -5,
  backgroundColor:"#D0CECE"
}));

export const ImageBox = styled("div")(() => ({
  textAlign: "center", 
}));

export const ImageBoxBotton = styled("div")(() => ({
  textAlign: "center", 
  cursor: "pointer"
}));
