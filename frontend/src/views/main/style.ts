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
}));

export const ImagePreviewBox = styled("div")(() => ({
marginTop: 10
}));

export const AddButtonBox = styled("div")(() => ({
textAlign: "center", 
marginTop: 10
}));

export const RegisterButtonBox = styled("div")(() => ({
  textAlign: "center", 
  marginTop: 10,
  marginBottom: 30
  }));
  