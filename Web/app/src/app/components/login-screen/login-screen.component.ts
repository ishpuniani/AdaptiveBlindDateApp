import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-login-screen',
  templateUrl: './login-screen.component.html',
  styleUrls: ['./login-screen.component.css']
})
export class LoginScreenComponent implements OnInit {

  isLoginScreen = true;

  constructor(private router: Router) { }

  ngOnInit() {
    
  }
  
  authenticateAndLogin(){
    this.router.navigateByUrl('home');
  }
  showSignUpContent(value){
    this.isLoginScreen = !value;
  }

}
