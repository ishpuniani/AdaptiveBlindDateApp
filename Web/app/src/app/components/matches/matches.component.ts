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
    this.matchData = [
      {
        'match_name' : "Ellen",
        'match_ph' : "2432534242",
        'activity_cat' : "Beach",
        'activity_name' : 'Blash Blah',
        'activity_add' : '123 ABC St, Dublin 2'
      },
      {
        'match_name' : "Mark",
        'match_ph' : "2432534242",
        'activity_cat' : "Beach",
        'activity_name' : 'Blash Blah',
        'activity_add' : '123 ABC St, Dublin 2'
      },
      {
        'match_name' : "Ella",
        'match_ph' : "3253454232",
        'activity_cat' : "Beach",
        'activity_name' : 'Blash wqrwsdw Blah',
        'activity_add' : '123 ABC St'
      },
      {
        'match_name' : "Mark Spencer",
        'match_ph' : "42354534423",
        'activity_cat' : "Beach",
        'activity_name' : 'Blash Blah',
        'activity_add' : 'Dublin 2'
      }
    ];
  }

  fetchMatchData(){
    this.userService.getMatches().subscribe((response)=>{
      this.matchData = response;
     });
  }

}
