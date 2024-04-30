

export function sign_up() {
  document.getElementById("RegisterButton").addEventListener("click", function (event) {

      const rol_ = document.getElementById('dropdownRol').value;
      const user_ = document.getElementById('user').value;
      const password_ = document.getElementById('passwordRegister').value;
      const email_ = document.getElementById('email').value;
      var er = false
  
      if (rol_.trim() === '' || user_.trim() === '' || password_.trim() === '') {
          Swal.fire({
              title: 'Faltan datos',
              text: 'Por favor, completa todos los campos',
              icon: 'error',
              backdrop: false,
              timer: 4500,
              timerProgressBar: true,
              confirmButtonColor: '#B70811'
          })
          er = true
      } else {
          er = false
      }  
      if (!er) {
          const dataToSend = {
              user: user_,
              password: password_,
              role: rol_,
              mail: email_,
          };
          fetch('/api/users/save', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(dataToSend)
          })
              .then(response => response.json())
              .then(data => {
                  if (data.error) {
                      Swal.fire({
                          title: data.error,
                          text: 'Ingresa otro valido',
                          icon: 'error',
                          backdrop: false,
                          timer: 7000,
                          timerProgressBar: true,
                          confirmButtonColor: '#B70811'
                      })
                  } else {
                      Swal.fire({
                          title: data.mensaje,
                          icon: 'success',
                          backdrop: false,
                          timer: 2000,
                          confirmButtonColor: '#B70811',
                          cancelButtonColor: '#000'
                      }).then((result) => {
                          window.location.href = "/sign_up";
                      });
                  }
  
              })
              .catch(error => console.error(error));
      }
  
      event.preventDefault();
  }); 
}


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
          if (data.error){
            Swal.fire({
              title: data.error,
              text: 'Credenciales incorrectas. Vuelve a intertarlo.',
              icon: 'error',
              backdrop: false,
              confirmButtonColor: "#b70811",
              timer: 7000,
              timerProgressBar: true,
            })
          }          
          else {            
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
              window.location.href = "/home";
            });           
          }            
        })
        .catch(error => console.error(error));
              
    });
}

