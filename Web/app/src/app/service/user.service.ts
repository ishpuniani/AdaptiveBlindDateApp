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
  questionUrl: string = "http://127.0.0.1:5000/questions";
  answerUrl: string = "http://127.0.0.1:5000/answer";
  recommendUrl: string = "http://127.0.0.1:5000/recommend/";
  swipeUrl: string = "http://127.0.0.1:5000/swipe";
  matchesUrl: string = "http://127.0.0.1:5000/matches/";

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
  public getUserQuestions(){
    return this.httpClient.get(this.questionUrl, {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }
  public submitUserResponse(obj){
    return this.httpClient.post(this.answerUrl, obj, {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }
  public getRecommendations(){
    return this.httpClient.get(this.recommendUrl+localStorage.getItem('token') , {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }

  public submitUserResponseSwipe(obj){
    return this.httpClient.post(this.swipeUrl , obj, {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }

  public getMatches(){
    return this.httpClient.get(this.matchesUrl+localStorage.getItem('token') , {
      headers: new HttpHeaders({
           'Content-Type':  'application/json',
         })
      });
  }
}
