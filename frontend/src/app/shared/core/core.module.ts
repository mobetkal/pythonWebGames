import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { MaterialModule } from '../ui-components/material.module';

import { FooterComponent } from './footer/footer.component';
import { NavbarComponent } from './navbar/navbar.component';

@NgModule({
  imports: [
    CommonModule,
    NgbModule,
    RouterModule,
    MaterialModule
  ],
  exports: [
    FooterComponent,
    NavbarComponent
  ],
  declarations: [
    FooterComponent,
    NavbarComponent
  ]
})
export class CoreLayoutModule {
}
