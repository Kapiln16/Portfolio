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
    }
    else{
        currmode = "light"
        document.querySelector("body").style.backgroundColor = "beige";
        document.querySelector("header").style.color = "grey";
        document.querySelector("#mode").style.backgroundColor = "beige";
        document.querySelector(".main").style.backgroundColor = "grey";
        document.querySelector(".loadline").style.backgroundColor = "grey";
    }

});

function calculateBMI() {
  const weight = parseFloat(document.getElementById("weight").value);
  const height = parseFloat(document.getElementById("height").value);

  if (weight > 0 && height > 0) {
    const bmi = weight / (height * height);
    document.getElementById("result").innerText = "Your BMI is: " + bmi.toFixed(2);
  } else {
    document.getElementById("result").innerText = "Please enter valid height and weight.";
  }
}
