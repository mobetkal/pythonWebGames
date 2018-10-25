import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app.component';

import { AppPagesModule } from './pages/app-pages.module';
import { AppRoutingModule } from './app-routing.module';
import { SharedModule } from './shared/shared.module';

import { AuthenticationService } from './shared/authentication/authentication.service';
import { AuthenticationGuard } from './shared/authentication/authentication.guard';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    NgbModule.forRoot(),
    SharedModule,
    AppPagesModule,
    AppRoutingModule
  ],
  providers: [
    AuthenticationService,
    AuthenticationGuard
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
