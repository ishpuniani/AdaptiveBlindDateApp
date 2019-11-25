import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './common-components/header/header.component';
import { FooterComponent } from './common-components/footer/footer.component';
import { CompatibilityChartComponent } from './common-components/compatibility-chart/compatibility-chart.component';
import { LoginScreenComponent } from './components/login-screen/login-screen.component';
import { PotentialMatchesComponent } from './components/potential-matches/potential-matches.component';
import { PreferencesComponent } from './components/preferences/preferences.component';
import { AppContainerComponent } from './components/app-container/app-container.component';
import { MatchesComponent } from './components/matches/matches.component';
import { QuestionaireComponent } from './components/questionaire/questionaire.component';
import { ProfileComponent } from './components/profile/profile.component';
import { SliderComponent } from './commmon-components/slider/slider.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    CompatibilityChartComponent,
    LoginScreenComponent,
    PotentialMatchesComponent,
    PreferencesComponent,
    AppContainerComponent,
    MatchesComponent,
    QuestionaireComponent,
    ProfileComponent,
    SliderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
