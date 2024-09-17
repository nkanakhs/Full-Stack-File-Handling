import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FileUploadService {
  private uploadUrl = 'http://localhost:5000/upload';  // API URL for file upload

  constructor(private http: HttpClient) { }

  uploadFile(file: File, description: string): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('description', description);

    // Authorization token
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

    return this.http.post(this.uploadUrl, formData, { headers });
  }
}
