import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService.register(this.username, this.password).subscribe(
      () => {
        this.router.navigate(['/login']); // Redirect to login page after registration
      },
      (error) => {
        console.error('Registration failed', error);
      }
    );
  }
}
