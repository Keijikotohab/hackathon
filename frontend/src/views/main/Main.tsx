import Header from "../component/header";
import React, { useEffect, useState } from "react";
import Divider from "@mui/material/Divider";
import { Typography } from "@mui/material";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import FileUploadIcon from '@mui/icons-material/FileUpload';
import AddIcon from '@mui/icons-material/Add';
import Alert from '@mui/material/Alert';
import { HeaderBox, Padding, MainBox, ImagePreviewBox, AddButtonBox } from './style';
import { DisplayedImage } from "../../types/types"


import { Api } from "../../api/Api"
let api = new Api();

const Main: React.FC = () => {
  const [name, setName] = React.useState(''); 
  const [image, setImage] = React.useState<File>();
  const [nameStatus, setNameStatus] = React.useState(0); //0：初期状態 1：未選択 2:20文字以上(Alert用)
  const [imageStatus, setImageStatus] = React.useState(0); //0：初期状態 1：未選択
  const [displayedImages, setDisplayedImages] = React.useState<DisplayedImage[]>([])

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const formatFileSize = (bytes: number, decimalPoint: number) => {
      if (bytes === 0) return '0 Bytes'
      const k = 1000
      const dm = decimalPoint || 2
      const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
      const i = Math.floor(Math.log(bytes) / Math.log(k))
      return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i]
    }
    if (event.currentTarget.files != null) {
      const fileImages = event.currentTarget.files
      setImage(event.currentTarget.files[0]);
      setDisplayedImages(
        Array.from(fileImages).map((file) => {
          return {
            url: window.URL.createObjectURL(file),
            size: formatFileSize(file.size, 1),
          }
        })
      )
    }
  }

  const upLoad =()=>{
    if (image === undefined || name === '' || name.length > 19 ){
      if (name === ''){
        setNameStatus(1)
      }else if(name.length > 19){
        setNameStatus(2)
      }
      if (image === undefined ){
        setImageStatus(1)
      }
      alert("入力に不備があります")
    }else{
    console.log(api.postImage(image as File)); 
    window.location.href = "/finish"
    }
  }

  return (
    <>
      <HeaderBox>
        <Header />
      </HeaderBox>
      <Padding />
      <MainBox>
        <Typography fontWeight="bold">新規追加フォーム</Typography>
        <Divider sx={{ fontWeight: "bold" }} />
        {nameStatus === 1?<Alert sx={{marginTop:1, width:"50%", marginBottom: -2}} severity="error">名前を入力してください</Alert>:nameStatus === 2?<Alert sx={{marginTop:1, width:"50%", marginBottom: -2}} severity="error">文字数は20文字以下でお願いします</Alert>:<div/>}
        <Typography sx={{ fontWeight: "bold", marginTop: 2 }}>名前(※20文字以下でお願いします)</Typography>
        <TextField
          sx={{ width: "100%", marginBottom: 2 }}
          id="outlined-size-small"
          size="small"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
        {imageStatus === 1?<Alert sx={{marginTop:1, width:"50%", marginBottom: 0}} severity="error">写真を選択してください</Alert>:<div/>}
        <Typography sx={{ fontWeight: "bold" }}>写真(※100M以下でお願いします)</Typography>
        <Button variant="outlined" color="inherit" component="label" startIcon={<FileUploadIcon />}>
          Upload
          <input hidden type="file" onChange={handleChange} accept="image/*" multiple={false} />
        </Button>
        <ImagePreviewBox>
          {displayedImages.map((displayedImage: any, index: any) => {
            return (
              <div key={`${index}-li`}>
                <img style={{ height: 200, marginRight: 20 }} src={displayedImage.url} alt="" key={`${index}-img`} />
                <p style={{ marginRight: 20 }}>{}</p>
              </div>
            )
          })}
        </ImagePreviewBox>
        <AddButtonBox>
          <Button onClick={()=>upLoad()} variant="outlined" color="inherit" component="label" startIcon={<AddIcon />}>
              追加
          </Button>
        </AddButtonBox>
      </MainBox>
    </>
  )
};


export default Main;
