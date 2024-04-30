const d = document,
      w = window

import {switchTab, countCharacters, setImage, login, switchTab2} from "../js/inicio.js"
import { signin, sign_up } from "./signin.js";


signin()
sign_up()
d.addEventListener("DOMContentLoaded", e => {


    //Seleccionar elementos
    const tabSignin = d.querySelector(".buttonIn");
    const tabSignup = d.querySelector(".buttonUp");
    const savedTab = localStorage.getItem('selectedTab');
    const heroImage = d.getElementById('hero-image');
    const buttonLogin = d.getElementById('buttonLogin');
    const buttonSale = d.getElementById('buttonSale');
    const buttonView = d.getElementById('buttonView');


    //Poner contenido según ultima escogencia del usuario
    if (savedTab) {
      switchTab(savedTab);
    } else {
      switchTab('In');
    }


    //Poner hero image según el contenido

    if(savedTab === 'In'){
        heroImage.setAttribute("src", "/static/assets/man2.webp");
    }else{
        heroImage.setAttribute("src", "/static/assets/manReci.png");

    }
  

    //eventos click para el renderizado del contenido
  
    tabSignin.addEventListener("click", e => {
        switchTab('In');
        heroImage.setAttribute("src", "/static/assets/man2.webp");
      });
      
      tabSignup.addEventListener("click", e => {
        switchTab('Up');
        heroImage.setAttribute("src", "/static/assets/manReci.png");
      });

      


    countCharacters('passwordRegister','iconToChange')

    buttonLogin.addEventListener("click", e => {
        login('username', 'password', 'incorrect');
    });

  });






