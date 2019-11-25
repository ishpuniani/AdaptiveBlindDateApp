import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FooterComponent } from './common-components/footer/footer.component';
import { LoginScreenComponent } from './components/login-screen/login-screen.component';
import { CompatibilityChartComponent } from './common-components/compatibility-chart/compatibility-chart.component';
import { PotentialMatchesComponent } from './components/potential-matches/potential-matches.component';
import { PreferencesComponent } from './components/preferences/preferences.component';
import { AppContainerComponent } from './components/app-container/app-container.component';
import { QuestionaireComponent } from './components/questionaire/questionaire.component';
import { MatchesComponent } from './components/matches/matches.component';
import { ProfileComponent } from './components/profile/profile.component';


const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginScreenComponent },
  // { path: 'preferences', component: PreferencesComponent},
  { path: 'home', component: AppContainerComponent, 
    children: [
      { path: '', redirectTo: 'potentialMatches', pathMatch: 'full' },
      { path: 'preferences', component: PreferencesComponent },
      { path: 'potentialMatches', component: PotentialMatchesComponent },
      { path: 'match', component: MatchesComponent },
      { path: 'question', component: QuestionaireComponent },
      { path: 'profile', component: ProfileComponent }
    ]
   }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { enableTracing: true } )],
  exports: [RouterModule]
})
export class AppRoutingModule { }
