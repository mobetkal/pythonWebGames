import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Injectable()
export class AuthenticationService {

  private authTokenName = 'AUTH_TOKEN';

  constructor(
    private http: HttpClient,
    private router: Router,
    private cookieService: CookieService
  ) {
  }

  getAuthToken() {
    return this.cookieService.get(this.authTokenName);
  }

  isAuthenticated(): boolean {
    return this.getAuthToken() !== '';
  }

  login(usernameOrEmail: string, password: string) {
    // TODO Backend authentication
  }

  logout() {
    this.cookieService.delete(this.authTokenName);
    window.location.reload();
    this.router.navigate(['/login'], { queryParams: { logoutSuccess: true } });
  }
}
