	
const d = document,
w = window




export function switchTab(tab) {
  const tabContents = d.querySelectorAll('.tab-content');
  tabContents.forEach(content => {
    content.classList.add('hidden');
    content.classList.remove('flex');
  });

  const selectedContent = d.querySelector(`#${tab}-content`);
  if (selectedContent) {
    selectedContent.classList.remove('hidden');
    selectedContent.classList.add('flex');
    saveContent(tab);
  }

  const tabLinks = d.querySelectorAll('.tab-link');
  tabLinks.forEach(link => {
    link.classList.remove('active');
  });

  const selectedLink = d.querySelector(`.button${tab}`);
  if (selectedLink) {
    selectedLink.classList.add('active');
  }
}




function saveContent(tab) {
  localStorage.setItem('selectedTab', tab);
}

export function setImage(element,route){
  element.setAttribute("src", route);

}

export function countCharacters(inputPassword, iconToChange) {
  const input = d.querySelector(`#${inputPassword}`);
  const icon = d.querySelector(`#${iconToChange}`);

  input.addEventListener("input", e => {
    const valueInput = input.value.trim();

    icon.classList.remove("fa-xmark", "fa-square", "fa-check","activeIcon","red","orange","green");

    if (valueInput.length > 0 && valueInput.length < 5) {
      icon.classList.add("fa-xmark","activeIcon","red");
    } else if (valueInput.length >= 5 && valueInput.length < 8) {
      icon.classList.add("fa-square","activeIcon","orange");
    } else if (valueInput.length >= 8) {
      icon.classList.add("fa-check","activeIcon","green");
    }
  });
}


const dataUsers = [
    {
        username: "mauriciod-molinap@unilibre.edu.co",
        password: "123456789"
    }
]


export function login(username, password, incorrect) {
    const inputUsername = d.getElementById(username).value;
    const inputPassword = d.getElementById(password).value;

    const usuarios = dataUsers; 
    usuarios.forEach(el=>{
        if(el.username === inputUsername && el.password === inputPassword){
            // window.location.href = 'http://127.0.0.1:5000/templates/home'
        }else {
            d.getElementById(incorrect).classList.remove('hidden');
        }
    })

}


