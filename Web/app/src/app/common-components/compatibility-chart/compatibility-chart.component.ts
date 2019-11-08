import { Component, OnInit } from '@angular/core';
import * as Chart from 'chart.js';

@Component({
  selector: 'app-compatibility-chart',
  templateUrl: './compatibility-chart.component.html',
  styleUrls: ['./compatibility-chart.component.css']
})
export class CompatibilityChartComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    var canvas = <HTMLCanvasElement> document.getElementById("mycanvas");
    var ctx = canvas.getContext('2d');
    var options = {
      scale: {
        // Hides the scale
        display: true
      }
    };
    var data = {
      labels: ['Humour', 'Adventurous', 'Socially Active', 'Optimist', 'Creative'],
      datasets: [{
        backgroundColor: "rgba(197, 168, 243, 0.5)",
        borderColor: "rgba(197, 168, 243, 0.5)",
        pointBackgroundColor: "rgba(197, 168, 243, 0.5)",
        label: "Ellen",
        data: [5, 3, 2, 1, 4]
      },
      {
        backgroundColor: "rgba(68, 153, 226, 0.5)",
        borderColor: "rgba(68, 153, 226, 0.5)",
        pointBackgroundColor: "rgba(68, 153, 226, 0.5)",
        label: "Brad",
        data: [4, 4, 1, 2, 2]
      }]
    };
    var myRadarChart = new Chart(ctx, {
      type: 'radar',
      data: data,
      options: options
    });
  }

}
