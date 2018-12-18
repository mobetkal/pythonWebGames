import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TetrisComponent } from './tetris/tetris.component';
import { FallingballsComponent } from './fallingballs/fallingballs.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [TetrisComponent,
  FallingballsComponent]
})
export class GamesModule { }
