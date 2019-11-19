import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CompatibilityChartComponent } from './compatibility-chart.component';

describe('CompatibilityChartComponent', () => {
  let component: CompatibilityChartComponent;
  let fixture: ComponentFixture<CompatibilityChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CompatibilityChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CompatibilityChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
