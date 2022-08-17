export class Api {
    //id:string;
    //password: string;
    
    /*constructor(id: string, password: string) {
        this.id = id;
        this.password = password;
    }*/

    postImage(file:File){
      const formData = new FormData();
      formData.append("file", file);
      fetch("http://127.0.0.1:5000/images", { method: "POST", body: formData });
    }
}    

