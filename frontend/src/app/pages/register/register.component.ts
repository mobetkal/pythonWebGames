import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { first } from 'rxjs/operators';

import { AuthenticationService } from '../../shared/authentication/authentication.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  signInForm: FormGroup;

  registerError = '';
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
        Validators.required, Validators.minLength(5)
      ]),
      'firstName': new FormControl(null, [
        Validators.required, Validators.minLength(3)
      ]),
      'lastName': new FormControl(null, [
        Validators.required, Validators.minLength(3)
      ]),
      'password': new FormControl(null, [
        Validators.required, Validators.minLength(5)
      ]),
      'confirmPassword': new FormControl(null, [
        Validators.required
      ])
    });
  }

  onSubmit() {
    if (this.signInForm.valid) {
      this.loading = true;
      this.authService.register(
        this.signInForm.value.login,
        this.signInForm.value.password,
        this.signInForm.value.firstName,
        this.signInForm.value.lastName
      )
        .pipe(first())
        .subscribe(
          () => {
            this.loading = false;
            this.successRedirect(true);
          },
          error => {
            this.loading = false;
            if (error.error.message) {
              this.registerError = error.error.message;
            } else {
              this.registerError = 'Unknown error. Please try again later.';
            }
          });
    }
  }

  successRedirect(replaceState: boolean) {
    const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '';
    this.router.navigate([returnUrl], {replaceUrl: replaceState});
  }

  passwordsIsCorrect() {
    return this.signInForm.controls['password'].valid
      && this.signInForm.controls['confirmPassword'].valid
      && this.signInForm.value.password === this.signInForm.value.confirmPassword;
  }
}
