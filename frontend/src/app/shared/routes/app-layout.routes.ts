import { Routes } from '@angular/router';

import { TetrisComponent } from '../../games/tetris/tetris.component';

import { StatisticsComponent } from '../../pages/statistics/statistics.component';

import { FallingballsComponent } from 'src/app/games/fallingballs/fallingballs.component';

// Routes for protected content.

export const APP_PROTECTED_ROUTES: Routes = [
  // GAMES
  {
    path: 'tetris',
    component: TetrisComponent
  },
{
  path: 'fallingballs',
  component: FallingballsComponent
},

  // OTHER
  {
    path: 'statistics',
    component: StatisticsComponent
  }
];
