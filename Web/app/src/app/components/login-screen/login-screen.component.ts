import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import { UserService } from '../../service/user.service'

@Component({
  selector: 'app-login-screen',
  templateUrl: './login-screen.component.html',
  styleUrls: ['./login-screen.component.css']
})
export class LoginScreenComponent implements OnInit {

  isLoginScreen = true;
  errorMsg: String ;
  user = {
    name :'',
    email : '',
    password : '',
    mobile: '',
    confirmPassword: ''
  };
  token: String;

  constructor(private router: Router, private userService: UserService) { }

  ngOnInit() {
    
  }
  
  authenticateAndLogin(){
    let userdata = {
      'email' : this.user.email,
      'password' : this.user.password
    }
    this.userService.authenticateUser(userdata).subscribe((reponse)=>{
      this.token = reponse['public_id'];
      localStorage.setItem('token', reponse['public_id']);
      this.router.navigateByUrl('home');
     }); 
  }
  
  showSignUpContent(value){
    this.errorMsg = '';
    this.isLoginScreen = !value;
    this.user = {
      name : '',
      email : '',
      password : '',
      mobile: '',
      confirmPassword: ''
    };
  }

  signupUser(){
    this.errorMsg = '';
    if(this.user.password == this.user.confirmPassword){
      let userdata = {
        'name' : this.user.name,
        'email' : this.user.email,
        'password' : this.user.password,
        'mobile' : this.user.mobile
      }
      this.userService.signupUser(userdata).subscribe((reponse)=>{
        this.token = reponse['public_id'];
        localStorage.setItem('token', reponse['public_id']);
       }); 
       this.showSignUpContent(false);
    }else{
      this.errorMsg = 'Password and Confirm Password are not same.';
    }
  }

}
