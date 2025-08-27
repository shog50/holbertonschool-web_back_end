export function uploadPhoto() {
  return new Promise((resolve) => {
    resolve({ body: 'photo-profile-1' });
  });
}

export function createUser() {
  return new Promise((resolve) => {
    resolve({ firstName: 'Guillaume', lastName: 'Salva' });
  });
}

