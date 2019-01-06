import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';

import { API_URL } from '../../env';

@Injectable()
export class AuthenticationService {

  private authTokenCookie = 'ng-security-token';
  private userNameCookie = 'ng-security-user';
  private displayNameCookie = 'ng-security-display';

  constructor(
    private http: HttpClient,
    private router: Router,
    private cookieService: CookieService
  ) {
  }

  getAuthToken() {
    return this.cookieService.get(this.authTokenCookie);
  }

  getUserLogin() {
    return this.cookieService.get(this.userNameCookie);
  }

  getUserDisplayName() {
    return this.cookieService.get(this.displayNameCookie);
  }

  isAuthenticated(): boolean {
    return this.getAuthToken() !== '';
  }

  login(login: string, password: string) {
    return this.http.post<any>(`${API_URL}/login`, { login: login.toLowerCase(), password: password })
      .pipe(map(response => {
        if (response) {
          // store token in cookie to keep user logged in between page refreshes
          this.cookieService.set(this.authTokenCookie, response.auth_token);
          this.cookieService.set(this.displayNameCookie, response.display_name);
          this.cookieService.set(this.userNameCookie, response.login);
        }

        return response;
      }));
  }

  logout() {
    this.cookieService.delete(this.authTokenCookie);
    this.cookieService.delete(this.userNameCookie);
    this.router.navigate(['/login'], { queryParams: { logoutSuccess: true } });
  }

  register(login: string, password: string, firstName: string, lastName: string) {
    return this.http.post<any>(`${API_URL}/register`, {
      login: login.toLowerCase(),
      password: password,
      first_name: firstName,
      last_name: lastName
    })
      .pipe(map(response => {
        if (response) {
          // store token in cookie to keep user logged in between page refreshes
          this.cookieService.set(this.authTokenCookie, response.auth_token);
          this.cookieService.set(this.displayNameCookie, response.display_name);
          this.cookieService.set(this.userNameCookie, response.login);
        }

        return response;
      }));
  }
}
