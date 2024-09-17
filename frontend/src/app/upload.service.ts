// upload.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  private apiUrl = 'http://localhost:5000';  // Adjust if necessary

  constructor(private http: HttpClient) {}

  // Fetch paginated uploads
  getUploads(page: number, limit: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/uploads?page=${page}&limit=${limit}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('authToken')}`
      }
    });
  }
}
