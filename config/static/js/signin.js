

export function signin() {
    document.getElementById("buttonLogin").addEventListener("click", function (event) {
        event.preventDefault();
        const user = document.getElementById('username').value;
        const password = document.getElementById('password').value;
      
        const userData = {
          user: user,
          password: password
        };
      
        fetch('/api/users/signin', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
        })
          .then(response => response.json())
          .then(data => {
            if (data.error) {
              Swal.fire({
                title: data.error,
                text: 'Credenciales incorrectas. Vuelve a intertarlo.',
                icon: 'error',
                backdrop: false,
                confirmButtonColor: "#b70811",
                timer: 7000,
                timerProgressBar: true,
              })
            } else {
            
                alert
              Swal.fire({
                title: data.mensaje,
                text: 'Inicio de sesión exitoso',
                icon: 'success',
                backdrop: false,
                confirmButtonColor: "#b70811",
                timer: 3500,
                customClass: {
                  confirmButton: 'custom-confirm-button-class'
                }
              }).then((result) => {
                window.location.href = "/home ";
              });           
            }            
          })
          .catch(error => console.error(error));
                
      });
}

