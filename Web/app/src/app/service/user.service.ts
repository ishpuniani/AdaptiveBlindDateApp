import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  baseUrl:string = "http://127.0.0.1:5000/login"; 
  getUserBaseUrl:string = "http://127.0.0.1:5000/users"; 
  signUpURL: string = "http://127.0.0.1:5000/signup"

  constructor(private httpClient : HttpClient) { }

  public authenticateUser(obj){
    return this.httpClient.post(this.baseUrl,obj, {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }

  public getUsers(){
    return this.httpClient.get(this.getUserBaseUrl, {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }
  public signupUser(obj){
    return this.httpClient.post(this.signUpURL,obj, {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }
}
