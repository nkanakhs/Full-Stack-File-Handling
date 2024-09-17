import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { DashboardComponent } from './dashboard/dashboard.component';  // Import Dashboard Component
import { AuthGuard } from './auth.guard';
import { UploadFileComponent } from './upload-file/upload-file.component';


const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'dashboard', component: DashboardComponent , canActivate: [AuthGuard]  },  // Add route for Dashboard
  { path: 'upload', component: UploadFileComponent, canActivate: [AuthGuard] },  // File upload route
  { path: '', redirectTo: '/login', pathMatch: 'full' } // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
