import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import { User } from './models/user';

@Component({
  selector: 'app-users',
  imports: [FormsModule],
  templateUrl: './users.html',
  styleUrl: './users.css'
})
export class Users {

  private http = inject(HttpClient);

  private apiUrl = 'http://127.0.0.1:8000/api/v1/users';

  users = signal<User[]>([]);
  loading = signal(false);
  error = signal('');

  editingId = signal<number | null>(null);

  name = signal('');
  email = signal('');

  constructor() {
    this.getUsers();
  }

  // GET
  getUsers() {
    this.http.get<User[]>(this.apiUrl).subscribe({
      next: users => this.users.set(users),
      error: () => this.error.set('Unable to load users')
    });
  }

  // CREATE / UPDATE
  saveUser() {

    const data = {
      name: this.name(),
      email: this.email()
    };

    if (!data.name || !data.email) {
      this.error.set('Name and email are required');
      return;
    }

    this.loading.set(true);
    this.error.set('');

    const id = this.editingId();

    const request = id
      ? this.http.put<User>(`${this.apiUrl}/${id}`, data)
      : this.http.post<User>(this.apiUrl, data);

    request.subscribe({
      next: user => {

        if (id) {
          this.users.update(users =>
            users.map(item =>
              item.id === user.id ? user : item
            )
          );
        } else {
          this.users.update(users => [...users, user]);
        }

        this.clearForm();
        this.loading.set(false);
      },

      error: error => {
        this.error.set(
          error.error?.detail || 'Unable to save user'
        );

        this.loading.set(false);
      }
    });
  }

  // EDIT
  editUser(user: User) {
    this.editingId.set(user.id);
    this.name.set(user.name);
    this.email.set(user.email);
  }

  // DELETE
  deleteUser(user: User) {

    if (!confirm(`Delete ${user.name}?`)) {
      return;
    }

    this.http.delete(`${this.apiUrl}/${user.id}`).subscribe({
      next: () => {
        this.users.update(users =>
          users.filter(item => item.id !== user.id)
        );
      },

      error: error => {
        this.error.set(
          error.error?.detail || 'Unable to delete user'
        );
      }
    });
  }

  // CANCEL
  clearForm() {
    this.editingId.set(null);
    this.name.set('');
    this.email.set('');
  }
}