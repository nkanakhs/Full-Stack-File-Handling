import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService.login(this.username, this.password).subscribe(
      (response: any) => {
        localStorage.setItem('authToken', response.token); // Store the token
        console.log("bhkame")
        this.router.navigate(['/dashboard']); // Redirect on successful login
      },
      (error) => {
        console.error('Login failed', error);
      }
    );
  }
}