import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { AuthenticationService } from '../../shared/authentication/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  defaultLoginSuccessRedirect = '/';

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private authService: AuthenticationService
  ) { }

  ngOnInit() {
    if (this.authService.isAuthenticated()) {
      this.successRedirect(true);
    }
  }

  successRedirect(replaceState: boolean) {
    const returnUrl = this.route.snapshot.queryParams['returnUrl'];
    if (returnUrl) {
      this.router.navigate([returnUrl], {replaceUrl: replaceState});
    } else {
      this.router.navigate([this.defaultLoginSuccessRedirect], {replaceUrl: replaceState});
    }
  }

}
