import axios from  "axios"
import { ImageName } from "../types/types"

export class Api {
    private imageDataList:any = []
    
  /*
    id:string;
    password: string;
    constructor(id: string, password: string) {
        this.id = id;
        this.password = password;
    }*/

    postImage(file:File){
      const header = { headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        "Access-Control-Allow-Origin": "*",
         }}
      const data = new FormData()
      data.append('file', file)
      const postImageUri = 'http://127.0.0.1/images'
      axios.post(postImageUri, data, header)
      .then(res => {
        this.imageDataList.push(res.data)
        console.log(this.imageDataList[0])
        console.log(this.imageDataList[0][0]["id"])
      }).catch(err => {
        console.log(err)
      })
      return this.imageDataList
    }

    /*

    postName(data:ImageName[]){
      const header = { headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        "Access-Control-Allow-Origin": "*",
         }}
      axios.post('http://127.0.0.1/name', {data},header);

*/


    postName(data:ImageName[]){
        const headers = {
          'Content-Type': 'application/json',
          'accept': 'application/json',
        }
        axios.post("http://127.0.0.1/name", 

         data
          
        ,{headers: headers})
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      }

    




}    

