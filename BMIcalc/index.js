let modebtn = document.querySelector("#mode");
let currmode = "light";

modebtn.addEventListener("click", () =>{
    if (currmode == "light"){
        currmode = "dark";
        document.querySelector("body").style.backgroundColor = "gray";
        document.querySelector("header").style.color = "beige";
        document.querySelector("#mode").style.backgroundColor = "gray";
        document.querySelector(".main").style.backgroundColor = "beige";
        document.querySelector(".loadline").style.backgroundColor = "beige";
        document.querySelector(".main").style.color = "gray";
        document.querySelector("#submit").style.backgroundColor = "gray";
        document.querySelector("#submit").style.color = "beige";
    }
    else{
        currmode = "light"
        document.querySelector("body").style.backgroundColor = "beige";
        document.querySelector("header").style.color = "gray";
        document.querySelector("#mode").style.backgroundColor = "beige";
        document.querySelector(".main").style.backgroundColor = "gray";
        document.querySelector(".loadline").style.backgroundColor = "gray";
        document.querySelector(".main").style.color = "beige";
        document.querySelector("#submit").style.backgroundColor = "beige";
        document.querySelector("#submit").style.color = "gray";

    }

});






function calculateBMI() {
  const weight = parseFloat(document.getElementById("weight").value);
  const height = parseFloat(document.getElementById("height").value);
  //const height1 = parseFloat(document.getElementById("height1").value);
  //const height2 = parseFloat(document.getElementById("height2").value);

  //mainheight = (height1 + height2/12)*2.54;  

  if (weight > 0 && height > 0) {
    const bmi = weight / ((height * height)/10000);
    document.getElementById("result").innerText = "Your BMI is: " + bmi.toFixed(2);
  } else {
    document.getElementById("result").innerText = "Please enter valid height and weight.";
  }
}
