import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/service/user.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-potential-matches',
  templateUrl: './potential-matches.component.html',
  styleUrls: ['./potential-matches.component.css']
})
export class PotentialMatchesComponent implements OnInit {

  chartData;
  userData;
  potentialMatchesData
  potentialMatchIndex = 0;
  showMessage = false;
  showMoreInfo = false;

  constructor(private userService: UserService, private router: Router) { }

  ngOnInit() {
    console.log('------', localStorage.getItem('token'));
    if(localStorage.getItem('token') && localStorage.getItem('token') != null){
      this.fetchRecommendations();
    }else{
      this.router.navigateByUrl('/login');
    }
  }

  fetchRecommendations(){
    this.userService.getRecommendations().subscribe((response)=>{
      this.userData = response['user_model'];
      this.potentialMatchesData = response['matches'];
      if(!response['matches'] || response['matches'].length == 0){
        this.showMessage = true;
      }
      this.createChartData(this.potentialMatchIndex);
     });
  }

  createChartData(index){
    this.chartData = {
      user : {
        id : '',
        name : '',
        data : []
      },
      match : {
        id : '',
        name : '',
        data : []
      }
    };
    this.chartData.user.data = [this.userData.agreeableness,
      this.userData.conscientiousness,
      this.userData.extraversion,
      this.userData.neuroticism,
      this.userData.openness];
    this.chartData.user.id = this.userData.public_id;
    this.chartData.user.name = this.userData.name;
    this.chartData.match.data = [this.potentialMatchesData[index].agreeableness,
      this.potentialMatchesData[index].conscientiousness,
      this.potentialMatchesData[index].extraversion,
      this.potentialMatchesData[index].neuroticism,
      this.potentialMatchesData[index].openness];
    this.chartData.match.id = this.potentialMatchesData[index].public_id;
    this.chartData.match.name = this.potentialMatchesData[index].name;
  }

  likeDislike(userResp){
    let resp = {
      "userid": localStorage.getItem('token'),
      "userid2": this.chartData.match.id,
      'swipe': userResp
    }
    this.userService.submitUserResponseSwipe(resp).subscribe((response)=>{
      console.log(response);
     });
    if(this.potentialMatchIndex < this.potentialMatchesData.length-1){
      this.showMoreInfo = false;
      this.potentialMatchIndex++;
      this.createChartData(this.potentialMatchIndex);
    }else{
      this.showMessage = true;
    }
    console.log(resp);
  }

  toggleShowMoreInfo(){
    this.showMoreInfo = !this.showMoreInfo;
  }

}
