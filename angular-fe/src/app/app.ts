import { Component, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from './user';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  private http = inject(HttpClient);

  users = signal<User[]>([]);
  loading = signal(false);
  error = signal('');

  ngOnInit() {
    this.getUsers();
  }

  getUsers() {
    this.loading.set(true);
    this.error.set('');

    this.http.get<User[]>('http://127.0.0.1:8000/users')
      .subscribe({
        next: (data) => {
          console.log("data", data)
          this.users.set(data);
          this.loading.set(false);
        },
        error: (error) => {
          console.error(error);
          this.error.set('Unable to connect to Python API');
          this.loading.set(false);
        }
      });
  }
}