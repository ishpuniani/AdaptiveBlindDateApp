import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/service/user.service';

@Component({
  selector: 'app-matches',
  templateUrl: './matches.component.html',
  styleUrls: ['./matches.component.css']
})
export class MatchesComponent implements OnInit {

  matchData;

  constructor(private userService: UserService) { }

  ngOnInit() {
    this.fetchMatchData();
  }

  fetchMatchData(){
    this.userService.getMatches().subscribe((response)=>{
      this.matchData = response;
     });
  }

}
