import { Component, OnInit } from '@angular/core';

import { User } from '../../models/user.model';

import { AuthenticationService } from '../../authentication/authentication.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  isAuthenticated = false;
  user: User = new User('Marcin');
  isCollapsed = true;

  constructor(private authService: AuthenticationService) { }

  ngOnInit() {
    this.isAuthenticated = this.authService.isAuthenticated();
  }

  logout() {
    this.authService.logout();
  }
}
