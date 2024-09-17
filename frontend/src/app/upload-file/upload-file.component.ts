import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-upload-file',
  templateUrl: './upload-file.component.html',
  styleUrls: ['./upload-file.component.css']
})
export class UploadFileComponent {
  file: File | null = null;
  previewUrl: string | ArrayBuffer | null = null;
  description: string = '';

  constructor(private http: HttpClient) {}

  // Handle file input change
  onFileChange(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length) {
      this.file = input.files[0];

      // Preview the image
      const reader = new FileReader();
      reader.onload = () => {
        this.previewUrl = reader.result;
      };
      reader.readAsDataURL(this.file);
    }
  }

  // Handle form submit
  onSubmit(): void {
    if (!this.file) {
      return;
    }

    const formData = new FormData();
    formData.append('file', this.file);
    formData.append('description', this.description);

    // Make HTTP request to upload the file
    this.http.post('http://localhost:5000/upload', formData, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('authToken')}`
      }
    }).subscribe(response => {
      console.log('File uploaded successfully', response);

      // Clear the form fields after a successful upload
      this.resetForm();
    }, error => {
      console.error('File upload failed', error);
    });
  }

  // Reset the form fields
  resetForm(): void {
    this.file = null;         // Clear the file
    this.description = '';    // Clear the description
    this.previewUrl = null;   // Clear the preview image URL

    // Optionally, reset the file input field in case it needs to be reset in the DOM
    const fileInput = document.querySelector('input[type="file"]') as HTMLInputElement;
    if (fileInput) {
      fileInput.value = '';   // Reset the file input field
    }
  }

}
