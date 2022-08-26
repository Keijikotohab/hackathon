import Header from "../component/header";
import React, { useEffect, useState } from "react";
import Divider from "@mui/material/Divider";
import { Typography } from "@mui/material";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import FileUploadIcon from '@mui/icons-material/FileUpload';
import AddIcon from '@mui/icons-material/Add';
import CircularProgress from '@mui/material/CircularProgress';
import Alert from '@mui/material/Alert';
import { HeaderBox, Padding, MainBox, ImagePreviewBox, AddButtonBox, RegisterButtonBox, ImageBox, } from './style';
import { DisplayedImage, DisplayedIndividualImage, ImageName } from "../../types/types"
import { Api } from "../../api/Api"
import Yane from "../../images/yane.png"
import SelectImage from "../../images/1.1gazousitei.png"
import UpBotton from "../../images/2.2up.png"
import TuikaBotton from "../../images/3.3tuika.png"
import Description from "../../images/yokomikuzikai.png"


let api = new Api();
const sleep = (ms:number) => new Promise((resolve) => setTimeout(resolve, ms));
let imageList:DisplayedIndividualImage[] = []
let ImageNameList:ImageName[] = []

const Main: React.FC = () => {
  const [nameList, setNameList] = React.useState({ 0: '', 1: '' , 2: '' , 3: '' , 4: '' , 5: '' , 6: '' }); 
  const [image, setImage] = React.useState<File>();
  const [nameStatus, setNameStatus] = React.useState(0); //0：初期状態 1：未選択 2:20文字以上(Alert用)
  const [imageStatus, setImageStatus] = React.useState(0); //0：初期状態 1：未選択
  const [screenStatus, setScreenStatus] = React.useState(0); //0：初期状態 1：未選択
  const [uploadStatus, setUploadStatus] = React.useState(0); //0：初期状態 1：未選択
  const [loadingStatus, setLoadingStatus] = React.useState(0); //0：初期状態 1：未選択
  const [displayedImages, setDisplayedImages] = React.useState<DisplayedImage[]>([])
  const [displayedIndividualImages, setDisplayedIndividualImages] = React.useState<DisplayedIndividualImage[]>([])

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
            image_path: window.URL.createObjectURL(file),
            size: formatFileSize(file.size, 1),
          }
        })
      )
    }
  }


  const upLoad =()=>{
    if (image === undefined){
      if (image === undefined ){
        setImageStatus(1)
      }
      alert("入力に不備があります")
    }else{
      (async () => { 
        setLoadingStatus(1)
        let IndividualImageList:any = api.postImage(image as File);
        await sleep(1000);
        console.log("IndividualImageList",IndividualImageList[0])
        IndividualImageList[0].map((value:any, index:any) => {
          console.log(value["id"],value["image_path"]);
          imageList.push({
            id:value["id"],
            image_path: value["image_path"],
            name: "string"})
        });
        console.log(imageList)
        await sleep(1000);
        setScreenStatus(1)
        console.log(screenStatus)
        setDisplayedIndividualImages(imageList)
        console.log(displayedIndividualImages)
    })();
    
    }
  }

  const register =()=>{
    if (image === undefined){
      alert("入力に不備があります")
    }else{
      (async () => { 
        
        setDisplayedIndividualImages(imageList)
        console.log(displayedIndividualImages)
        console.log(nameList)
        
        displayedIndividualImages.map((value:any, index:any) => {
          console.log(value["id"],value["image_path"]);
          
          ImageNameList.push({
            id:value["id"],
            name: nameList[index===0?"0":index===1?"1":index===2?"2":index===3?"3":index===4?"4":index===5?"5":"6"]
          })
        });
        setUploadStatus(1)
        console.log(ImageNameList)
        api.postName(ImageNameList);

        await sleep(1000);
        window.location.href = "/finish"
    })();
    }
  }


  return (
    <>

      <ImageBox>
          <img style={{ width:"100%", marginRight: 0 }}  src={Yane} />
      </ImageBox>
      {uploadStatus===0?
        <ImageBox>
          <img style={{ width:700, marginRight: 0 }}  src={SelectImage} />
      </ImageBox>:<div/>
        }
      

      <Padding />
      <MainBox>
        {screenStatus===0?
        <>
          <ImageBox>
            <Button sx={{marginTop:-15}} color="inherit" component="label" >
            <img style={{ width:450, marginRight: 0 }}  src={UpBotton} />
              <input hidden type="file" onChange={handleChange} accept="image/*" multiple={false} />
            </Button>
          </ImageBox>
          
          <ImagePreviewBox>
            {displayedImages.map((displayedImage: any, index: any) => {
              return (
                <div key={`${index}-li`}>
                  <img style={{ width:"100%", marginRight: 20, marginBottom:50, marginTop:-30 }} src={displayedImage.image_path} alt="" key={`${index}-img`} />
                </div>
              )
            })}
          </ImagePreviewBox>
          <AddButtonBox>
            {loadingStatus===1?<CircularProgress />:
              <Button onClick={()=>upLoad()} color="inherit" component="label">
                  <img style={{ width:120, marginRight: 0,marginTop:-45 }}  src={TuikaBotton} />
              </Button>
            }
          </AddButtonBox>
        </>:<div/>
        }

        {screenStatus===1?
        <>
          <ImagePreviewBox>
            {imageList.map((urlimage: any, index: any) => {
              return (
                <div key={`${index}-li`}>
                  <img style={{ width:"100%", marginRight: 20 }} src={urlimage.image_path} alt="" key={`${index}-img`} />
                  <p style={{ marginRight: 20 }}>{urlimage.string}</p>
                  {nameStatus === 1?<Alert sx={{marginTop:1, width:"50%", marginBottom: -2}} severity="error">名前を入力してください</Alert>:nameStatus === 2?<Alert sx={{marginTop:1, width:"50%", marginBottom: -2}} severity="error">文字数は20文字以下でお願いします</Alert>:<div/>}
                  <Typography sx={{ fontWeight: "bold", marginTop: 0 }}>名前(※20文字以下でお願いします)</Typography>
                  <TextField
                    sx={{ width: "100%", marginBottom: 2 }}
                    id="outlined-size-small"
                    size="small"
                    value={nameList[index===0?"0":index===1?"1":index===2?"2":index===3?"3":index===4?"4":index===5?"5":"6"]}
                    onChange={(event) => setNameList((index===0?{ ...nameList, 0:event.target.value }:index===1?{ ...nameList, 1:event.target.value }:index===2?{ ...nameList, 2:event.target.value }:index===3?{ ...nameList, 3:event.target.value }:index===4?{ ...nameList, 4:event.target.value }:index===5?{ ...nameList, 5:event.target.value }:{ ...nameList, 6:event.target.value }))}
                  />
                </div>
              )
            })}
          </ImagePreviewBox>
          <RegisterButtonBox>
          {uploadStatus===1?<CircularProgress />:
              <Button onClick={()=>register()} variant="outlined" color="inherit" component="label" startIcon={<AddIcon />}>
                  登録
              </Button>
            }
          </RegisterButtonBox>
        </>
        :
        <div/>}
        </MainBox>
        {uploadStatus===0?
        <ImageBox>
          <img style={{ width:850, marginRight: 0 }}  src={Description} />
        </ImageBox>:<div/>
        }

      </>

  )
};


export default Main;
