import { Component, DoCheck } from '@angular/core';

import { AuthenticationService } from '../../authentication/authentication.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css',
'./css/fontello.css']
})
export class NavbarComponent implements DoCheck {
  isAuthenticated = false;
  displayName = '';
  isCollapsed = true;

  constructor(private authService: AuthenticationService) { }

  logout() {
    this.authService.logout();
  }

  ngDoCheck() {
    this.isAuthenticated = this.authService.isAuthenticated();
    this.displayName = this.authService.getUserName();
  }
}
