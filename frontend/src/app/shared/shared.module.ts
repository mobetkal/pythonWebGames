import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CoreLayoutModule } from './core/core.module';
import { MaterialModule } from './ui-components/material.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';
import { GamesModule } from '../games/games.module';

import { CookieService } from 'ngx-cookie-service';

@NgModule({
  imports: [
    CommonModule,
    NgbModule,
    MaterialModule,
    CoreLayoutModule,
    GamesModule
  ],
  exports: [
    RouterModule,
    NgbModule,
    MaterialModule,
    CoreLayoutModule,
    CommonModule
  ],
  providers: [
    CookieService
  ],
  declarations: []
})
export class SharedModule { }
