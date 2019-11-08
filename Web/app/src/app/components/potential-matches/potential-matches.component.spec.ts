import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PotentialMatchesComponent } from './potential-matches.component';

describe('PotentialMatchesComponent', () => {
  let component: PotentialMatchesComponent;
  let fixture: ComponentFixture<PotentialMatchesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PotentialMatchesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PotentialMatchesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
