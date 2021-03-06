import { Component, OnInit, Input, SimpleChanges } from '@angular/core';
import * as Chart from 'chart.js';

@Component({
  selector: 'app-compatibility-chart',
  templateUrl: './compatibility-chart.component.html',
  styleUrls: ['./compatibility-chart.component.css']
})
export class CompatibilityChartComponent implements OnInit {

  @Input() chartData;
  constructor() { }

  ngOnInit() {
    console.log(this.chartData);
    var canvas = <HTMLCanvasElement> document.getElementById("mycanvas");
    var ctx = canvas.getContext('2d');
    var options = {
      scale: {
        // Hides the scale
        display: true
      }
    };
    if(this.chartData && this.chartData.user && this.chartData.match){
      var data = {
        labels: ['Agreeableness', 'Conscientiousness', 'Extraversion', 'Neuroticism', 'Openness'],
        datasets: [{
          backgroundColor: "rgba(230, 15, 15, 0.3)",
          borderColor: "rgba(230, 15, 15, 0.3)",
          pointBackgroundColor: "rgba(230, 15, 15, 0.3)",
          label: this.chartData.user.name,
          data: this.chartData.user.data
        },
        {
          backgroundColor: "rgba(0, 123, 255, 0.3)",
          borderColor: "rgba(0, 123, 255, 0.3)",
          pointBackgroundColor: "rgba(0, 123, 255, 0.3)",
          label: this.chartData.match.name,
          data: this.chartData.match.data
        }]
      };
      var myRadarChart = new Chart(ctx, {
        type: 'radar',
        data: data,
        options: options
      });
    }
  } 

  ngOnChanges(changes: SimpleChanges) {
    this.ngOnInit();
  }

}
