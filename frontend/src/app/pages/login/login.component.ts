import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';

import { AuthenticationService } from '../../shared/authentication/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  signInForm: FormGroup;

  loginError = '';
  loading = false;

  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private authService: AuthenticationService
  ) { }

  ngOnInit() {
    if (this.authService.isAuthenticated()) {
      this.successRedirect(true);
    }

    this.signInForm = new FormGroup({
      'login': new FormControl(null, [
        Validators.required
      ]),
      'password': new FormControl(null, [
        Validators.required
      ])
    });
  }

  onSubmit() {
    if (this.signInForm.valid) {
      this.loading = true;
      this.authService.login(this.signInForm.value.login, this.signInForm.value.password)
        .pipe(first())
        .subscribe(
          () => {
            this.loading = false;
            this.successRedirect(true);
          },
          error => {
            this.loading = false;
            if (error.error.message) {
              this.loginError = error.error.message;
            } else {
              this.loginError = 'Unknown error. Please try again later.';
            }
          });
    }
  }

  successRedirect(replaceState: boolean) {
    const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '';
    this.router.navigate([returnUrl], {replaceUrl: replaceState});
  }

}
