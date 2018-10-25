import { Routes } from '@angular/router';

import { TetrisComponent } from '../../games/tetris/tetris.component';

import { StatisticsComponent } from '../../pages/statistics/statistics.component';

// Routes for protected content.

export const APP_PROTECTED_ROUTES: Routes = [
  // GAMES
  {
    path: 'tetris',
    component: TetrisComponent
  },

  // OTHER
  {
    path: 'statistics',
    component: StatisticsComponent
  }
];
