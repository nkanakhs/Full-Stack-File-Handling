import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  uploads: any[] = [];
  currentPage = 1;
  totalPages = 1;
  limit = 10; // Files per page

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.getUploads(this.currentPage); // Fetch uploads on initialization
  }

  // Fetch paginated uploads from the server
  getUploads(page: number): void {
    this.http.get(`http://localhost:5000/uploads?page=${page}&limit=${this.limit}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('authToken')}`
      }
    }).subscribe(
      (response: any) => {
        this.uploads = response.uploads;
        this.totalPages = response.total_pages;
      },
      (error) => {
        console.error('Failed to fetch uploads', error);
      }
    );
  }

  // Handle pagination change
  onPageChange(newPage: number): void {
    if (newPage >= 1 && newPage <= this.totalPages) {
      this.currentPage = newPage;
      this.getUploads(this.currentPage);  // Fetch uploads for the new page
    }
  }
}
