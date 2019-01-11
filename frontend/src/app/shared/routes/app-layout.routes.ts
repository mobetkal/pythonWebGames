import { Routes } from '@angular/router';

import { FallingBallsComponent } from '../../games/falling-balls/falling-balls.component';
import { McBirdComponent } from 'src/app/games/mc-bird/mc-bird.component';

import { StatisticsComponent } from '../../pages/statistics/statistics.component';

// Routes for protected content.

export const APP_PROTECTED_ROUTES: Routes = [
  // GAMES
  {
    path: 'falling-balls',
    component: FallingBallsComponent
  },

  {
    path: 'mc-bird',
    component: McBirdComponent
  },

  // OTHER
  {
    path: 'statistics',
    component: StatisticsComponent
  }
];
