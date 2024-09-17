import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  title = 'Dash';

  constructor(private router: Router, private authService: AuthService) {}
  
  logout() {
    this.authService.logout();  // Implement this in AuthService
    localStorage.removeItem('authToken');  // Remove the token
    this.router.navigate(['/login']);  // Redirect to login page
  }


  isAuthenticated(): boolean {
    return this.authService.isAuthenticated();
  }

  isLoginPage(): boolean {
    return this.router.url === '/login' || this.router.url === '/register';
  }
}
