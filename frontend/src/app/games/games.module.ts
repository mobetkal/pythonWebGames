import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FallingBallsComponent } from './falling-balls/falling-balls.component';
import { McBirdComponent } from './mc-bird/mc-bird.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [
    FallingBallsComponent,
    McBirdComponent
  ]
})
export class GamesModule { }
