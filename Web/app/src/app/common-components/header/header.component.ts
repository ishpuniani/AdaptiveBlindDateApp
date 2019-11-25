import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  showMenuDropdown = false;

  constructor(private router: Router) { }

  ngOnInit() {
  }

  showHideMenuDropdown(){
    this.showMenuDropdown = !this.showMenuDropdown;
  }

  navigate(route) {
    this.showMenuDropdown = false;
    this.router.navigateByUrl('/'+route);
  }

}
