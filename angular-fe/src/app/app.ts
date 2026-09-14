import { Component, inject, OnInit, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { User } from './user';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.css',
  imports: [FormsModule]
})
export class App implements OnInit {

  private http = inject(HttpClient);

  private apiUrl = 'http://127.0.0.1:8000/users';

  users = signal<User[]>([]);

  loading = signal(false);

  error = signal('');

  editingUserId = signal<number | null>(null);

  formName = signal('');

  formEmail = signal('');


  // --------------------------------------------------
  // INIT
  // --------------------------------------------------

  ngOnInit() {
    this.getUsers();
  }


  // --------------------------------------------------
  // GET USERS
  // --------------------------------------------------

  getUsers() {

    this.loading.set(true);
    this.error.set('');

    this.http.get<User[]>(this.apiUrl)
      .subscribe({

        next: (data) => {

          console.log('Users:', data);

          this.users.set(data);

          this.loading.set(false);
        },

        error: (error) => {

          console.error(error);

          this.error.set(
            'Unable to connect to Python API'
          );

          this.loading.set(false);
        }

      });
  }


  // --------------------------------------------------
  // CREATE USER
  // --------------------------------------------------

  createUser() {

    const name = this.formName().trim();
    const email = this.formEmail().trim();

    if (!name || !email) {
      this.error.set('Name and email are required');
      return;
    }

    this.loading.set(true);
    this.error.set('');

    const newUser = {
      name,
      email
    };

    this.http.post<User>(this.apiUrl, newUser)
      .subscribe({

        next: (user) => {

          console.log('Created:', user);

          this.users.update(users => [
            ...users,
            user
          ]);

          this.clearForm();

          this.loading.set(false);
        },

        error: (error) => {

          console.error(error);

          this.error.set(
            error.error?.detail ||
            'Unable to create user'
          );

          this.loading.set(false);
        }

      });
  }


  // --------------------------------------------------
  // START EDIT
  // --------------------------------------------------

  editUser(user: User) {

    this.editingUserId.set(user.id);

    this.formName.set(user.name);

    this.formEmail.set(user.email);

    this.error.set('');
  }


  // --------------------------------------------------
  // UPDATE USER
  // --------------------------------------------------

  updateUser() {

    const userId = this.editingUserId();

    if (userId === null) {
      return;
    }

    const name = this.formName().trim();
    const email = this.formEmail().trim();

    if (!name || !email) {
      this.error.set('Name and email are required');
      return;
    }

    this.loading.set(true);
    this.error.set('');

    const updatedUser = {
      name,
      email
    };

    this.http.put<User>(
      `${this.apiUrl}/${userId}`,
      updatedUser
    )
      .subscribe({

        next: (user) => {

          console.log('Updated:', user);

          this.users.update(users =>
            users.map(existingUser =>
              existingUser.id === user.id
                ? user
                : existingUser
            )
          );

          this.clearForm();

          this.loading.set(false);
        },

        error: (error) => {

          console.error(error);

          this.error.set(
            error.error?.detail ||
            'Unable to update user'
          );

          this.loading.set(false);
        }

      });
  }


  // --------------------------------------------------
  // DELETE USER
  // --------------------------------------------------

  deleteUser(user: User) {

    const confirmed = confirm(
      `Are you sure you want to delete ${user.name}?`
    );

    if (!confirmed) {
      return;
    }

    this.loading.set(true);
    this.error.set('');

    this.http.delete(
      `${this.apiUrl}/${user.id}`
    )
      .subscribe({

        next: (response) => {

          console.log('Deleted:', response);

          this.users.update(users =>
            users.filter(
              existingUser =>
                existingUser.id !== user.id
            )
          );

          this.loading.set(false);
        },

        error: (error) => {

          console.error(error);

          this.error.set(
            error.error?.detail ||
            'Unable to delete user'
          );

          this.loading.set(false);
        }

      });
  }


  // --------------------------------------------------
  // CANCEL EDIT
  // --------------------------------------------------

  cancelEdit() {

    this.clearForm();
  }


  // --------------------------------------------------
  // CLEAR FORM
  // --------------------------------------------------

  clearForm() {
    this.editingUserId.set(null);
    this.formName.set('');
    this.formEmail.set('');
    this.error.set('');
  }
}